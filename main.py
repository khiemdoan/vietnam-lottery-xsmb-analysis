
__author__ = 'KhiemDH'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

import logging
from datetime import date, datetime, time, timedelta
from pathlib import Path
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
from cloudscraper import CloudScraper
from pytz import timezone
from jinja2 import Environment, FileSystemLoader, select_autoescape


def load_results(path: Path) -> pd.DataFrame:
    try:
        results = pd.read_csv(path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        columns=[
            'date',
            'special',
            'prize1',
            'prize2_1', 'prize2_2',
            'prize3_1', 'prize3_2', 'prize3_3', 'prize3_4', 'prize3_5', 'prize3_6',
            'prize4_1', 'prize4_2', 'prize4_3', 'prize4_4',
            'prize5_1', 'prize5_2', 'prize5_3', 'prize5_4', 'prize5_5', 'prize5_6',
            'prize6_1', 'prize6_2', 'prize6_3',
            'prize7_1', 'prize7_2', 'prize7_3', 'prize7_4',
        ]
        results = pd.DataFrame(columns=columns)

    results['date'] = pd.to_datetime(results['date'])
    results.iloc[:, 1:] = results.iloc[:, 1:].astype('int64')
    # results.set_index('date', inplace=True)
    return results


def fetch_result(selected_date: date) -> pd.DataFrame:
    url = f'https://xoso.com.vn/xsmb-{selected_date:%d-%m-%Y}.html'
    scraper = CloudScraper()
    response = scraper.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    prizes = soup.find_all(attrs={'class': 'special-prize'})
    special = [int(p.text) for p in prizes]
    prizes = soup.find_all(attrs={'class': 'prize1'})
    prize1 = [int(p.text) for p in prizes]
    prizes = soup.find_all(attrs={'class': 'prize2'})
    prize2 = [int(p.text) for p in prizes]
    prizes = soup.find_all(attrs={'class': 'prize3'})
    prize3 = [int(p.text) for p in prizes]
    prizes = soup.find_all(attrs={'class': 'prize4'})
    prize4 = [int(p.text) for p in prizes]
    prizes = soup.find_all(attrs={'class': 'prize5'})
    prize5 = [int(p.text) for p in prizes]
    prizes = soup.find_all(attrs={'class': 'prize6'})
    prize6 = [int(p.text) for p in prizes]
    prizes = soup.find_all(attrs={'class': 'prize7'})
    prize7 = [int(p.text) for p in prizes]
    df = pd.DataFrame({
        'date': [selected_date],
        'special': [special[0]],
        'prize1': [prize1[0]],
        'prize2_1': [prize2[0]], 'prize2_2': [prize2[1]],
        'prize3_1': [prize3[0]], 'prize3_2': [prize3[1]], 'prize3_3': [prize3[2]], 'prize3_4': [prize3[3]], 'prize3_5': [prize3[4]], 'prize3_6': [prize3[5]],
        'prize4_1': [prize4[0]], 'prize4_2': [prize4[1]], 'prize4_3': [prize4[2]], 'prize4_4': [prize4[3]],
        'prize5_1': [prize5[0]], 'prize5_2': [prize5[1]], 'prize5_3': [prize5[2]], 'prize5_4': [prize5[3]], 'prize5_5': [prize5[4]], 'prize5_6': [prize5[5]],
        'prize6_1': [prize6[0]], 'prize6_2': [prize6[1]], 'prize6_3': [prize6[2]],
        'prize7_1': [prize7[0]], 'prize7_2': [prize7[1]], 'prize7_3': [prize7[2]], 'prize7_4': [prize7[3]],
    })
    df['date'] = pd.to_datetime(df['date'])
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('int64')
    # df.set_index('date', inplace=True)
    return df


if __name__ == '__main__':
    file_path = 'results/xsmb.csv'

    results = load_results(file_path)
    print(f'Loaded data: {results.shape}')

    start_date = results['date'].max()
    if pd.isnull(start_date):
        start_date = date(2010, 1, 1)
    else:
        start_date = start_date.to_pydatetime()
        start_date += timedelta(days=1)
        start_date = start_date.date()

    tz = timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)

    last_date = now.date()
    if now.time() < time(18, 35):
        last_date -= timedelta(days=1)

    delta = (last_date - start_date).days + 1
    for i in range(delta):
        selected_date = start_date + timedelta(days=i)
        if pd.to_datetime(selected_date) in results.index:
            continue
        print(f'Fetching: {selected_date}')
        try:
            row = fetch_result(selected_date)
            print(row.iloc[0].tolist())
        except Exception as ex:
            logging.exception(ex)
        results = pd.concat([results, row])
        sleep(0.1)

    results.to_csv(file_path, index=False)
    print(f'Saved data: {results.shape}')

    last_date = pd.to_datetime(last_date)
    start_date = pd.Timestamp(year=last_date.year-1, month=last_date.month, day=last_date.day)

    small_results = results[(start_date < results['date']) & (results['date'] <= last_date)]
    small_results.to_csv('results/xsmb_1_year.csv', index=False)

    recent_results = small_results.iloc[-1].values[1:]
    recent_results = recent_results % 100
    loto_result = []
    for i in range(10):
        category = sorted([d for d in recent_results if d // 10 == i])
        category = [f'{d%10:1d}' for d in category]
        category = ', '.join(category)
        loto_result.append(category)

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape()
    )
    template = env.get_template('README.j2')
    content = template.render(loto_result=loto_result, **small_results.iloc[-1])
    with open('README.md', 'w') as outfile:
        outfile.write(content)
