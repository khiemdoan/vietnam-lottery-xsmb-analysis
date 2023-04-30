
__author__ = 'KhiemDH'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

import logging
from datetime import date, datetime, time, timedelta
from pathlib import Path
from time import sleep

import numpy as np
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
from cloudscraper import CloudScraper
from jinja2 import Environment, FileSystemLoader, select_autoescape
from matplotlib import pyplot as plt
from pytz import timezone


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
    return results


def load_sparse_results(path: Path) -> pd.DataFrame:
    try:
        results = pd.read_csv(path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        columns = ['date'] + [i for i in range(100)]
        results = pd.DataFrame(columns=columns)

    results['date'] = pd.to_datetime(results['date'])
    results.iloc[:, 1:] = results.iloc[:, 1:].astype('float64')
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
    return df


def download_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    file_path = 'results/xsmb.csv'
    sparse_file_path = 'results/xsmb_sparse.csv'

    results = load_results(file_path)
    sparse_results = load_sparse_results(sparse_file_path)

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

            sparse = pd.concat([row.iloc[-1:, 0:1], pd.DataFrame(np.zeros((1, 100)))], axis=1)
            numbers = row.iloc[-1, 1:] % 100
            counts = numbers.value_counts()
            for k, v in counts.items():
                sparse[str(k)] = pd.to_numeric(v)

            results = pd.concat([results, row])
            sparse_results = pd.concat([sparse_results, sparse])
        except Exception as ex:
            logging.exception(ex)
        sleep(0.1)

    results.to_csv(file_path, index=False)
    sparse_results.to_csv(sparse_file_path, index=False)
    print(f'Saved data: {results.shape}')

    last_date = pd.to_datetime(last_date)

    start_date = pd.Timestamp(year=last_date.year-5, month=last_date.month, day=last_date.day)
    results_5_year = results[(start_date < results['date']) & (results['date'] <= last_date)]
    results_5_year.reset_index(drop=True, inplace=True)
    results_5_year.to_csv('results/xsmb_5_year.csv', index=False)

    start_date = pd.Timestamp(year=last_date.year-3, month=last_date.month, day=last_date.day)
    results_3_year = results[(start_date < results['date']) & (results['date'] <= last_date)]
    results_3_year.reset_index(drop=True, inplace=True)
    results_3_year.to_csv('results/xsmb_3_year.csv', index=False)

    start_date = pd.Timestamp(year=last_date.year-2, month=last_date.month, day=last_date.day)
    results_2_year = results[(start_date < results['date']) & (results['date'] <= last_date)]
    results_2_year.reset_index(drop=True, inplace=True)
    results_2_year.to_csv('results/xsmb_2_year.csv', index=False)

    start_date = pd.Timestamp(year=last_date.year-1, month=last_date.month, day=last_date.day)
    small_results = results[(start_date < results['date']) & (results['date'] <= last_date)]
    small_results.reset_index(drop=True, inplace=True)
    small_results.to_csv('results/xsmb_1_year.csv', index=False)

    return results, sparse_results


def colors_from_values(values, palette_name):
    normalized = (values - min(values)) / (max(values) - min(values))
    indices = np.round(normalized * (len(values) - 1)).astype(np.int32)
    palette = sns.color_palette(palette_name, len(values))
    return np.array(palette).take(indices, axis=0)


def last_appearing(data: pd.DataFrame, type: str):
    numbers = data[['special']]
    numbers.reset_index(inplace=True)
    predict_index = numbers['index'].max() + 1

    numbers = numbers.melt(id_vars='index', var_name='prize', value_name='value')
    numbers['value'] = numbers['value'] % 100
    last_appearing = numbers.groupby(['value'])['index'].max()
    last_appearing = last_appearing.to_frame()
    last_appearing.reset_index()
    last_appearing['delta'] = predict_index - last_appearing['index']
    last_appearing.drop('index', axis=1, inplace=True)

    heatmap_data = last_appearing.copy()
    heatmap_data['tens'] = heatmap_data.index // 10
    heatmap_data['ones'] = heatmap_data.index % 10
    heatmap_data = heatmap_data[['tens', 'ones', 'delta']]
    heatmap_data = heatmap_data.pivot(index='tens', columns='ones', values='delta')

    bar_data = last_appearing.sort_values('delta', ascending=False)
    bar_data = bar_data.iloc[:10, :]
    bar_data.reset_index(inplace=True)
    bar_data = bar_data.rename(columns = {'index': 'value'})
    bar_data['value'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn', ax=ax)
    ax.set_title('Delta')
    fig.savefig('images/special_delta.jpg')

    fig, ax = plt.subplots()
    palette = reversed(colors_from_values(bar_data['delta'], 'summer'))
    sns.barplot(bar_data, x='value', y='delta', palette=palette, ax=ax)
    for bar in ax.containers:
        ax.bar_label(bar, fmt='%d')
    ax.set_title('Top 10')
    fig.savefig('images/special_delta_top_10.jpg')


def last_appearing_loto(data):
    numbers = data.drop('date', axis=1)
    numbers.reset_index(inplace=True)

    predict_index = numbers['index'].max() + 1

    numbers = numbers.melt(id_vars='index', var_name='prize', value_name='value')
    numbers['value'] = numbers['value'] % 100
    last_appearing = numbers.groupby(['value'])['index'].max()
    last_appearing = last_appearing.to_frame()
    last_appearing.reset_index()
    last_appearing['delta'] = predict_index - last_appearing['index']
    last_appearing.drop('index', axis=1, inplace=True)

    heatmap_data = last_appearing.copy()
    heatmap_data['tens'] = heatmap_data.index // 10
    heatmap_data['ones'] = heatmap_data.index % 10
    heatmap_data = heatmap_data[['tens', 'ones', 'delta']]
    heatmap_data = heatmap_data.pivot(index='tens', columns='ones', values='delta')

    bar_data = last_appearing.sort_values('delta', ascending=False)
    bar_data = bar_data.iloc[:10, :]
    bar_data.reset_index(inplace=True)
    bar_data = bar_data.rename(columns = {'index': 'value'})
    bar_data['value'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn', ax=ax)
    ax.set_title('Delta')
    fig.savefig('images/delta.jpg')

    fig, ax = plt.subplots()
    palette = reversed(colors_from_values(bar_data['delta'], 'summer'))
    sns.barplot(bar_data, x='value', y='delta', palette=palette, ax=ax)
    for bar in ax.containers:
        ax.bar_label(bar, fmt='%d')
    ax.set_title('Top 10')
    fig.savefig('images/delta_top_10.jpg')


if __name__ == '__main__':
    results, sparse_results = download_data()

    last_date = results['date'].max()

    start_date = pd.Timestamp(year=last_date.year-2, month=last_date.month, day=last_date.day)
    results_2_year = results[(start_date < results['date']) & (results['date'] <= last_date)]
    results_2_year.reset_index(drop=True, inplace=True)
    start_date = pd.Timestamp(year=last_date.year-1, month=last_date.month, day=last_date.day)
    small_results = results[(start_date < results['date']) & (results['date'] <= last_date)]
    small_results.reset_index(drop=True, inplace=True)
    small_results.to_csv('results/xsmb_1_year.csv', index=False)

    # Last appearing Special price
    last_appearing(results_2_year, 'tail_special')

    recent_results = small_results.iloc[-1].values[1:]
    recent_results = recent_results % 100
    loto_result = []
    for i in range(10):
        category = sorted([d for d in recent_results if d // 10 == i])
        category = [f'{d%10:1d}' for d in category]
        category = ', '.join(category) if len(category) > 0 else '-'
        loto_result.append(category)

    numbers = small_results.drop(columns=['date'])
    numbers = numbers % 100
    numbers = numbers.stack()

    counts = numbers.value_counts()
    max_count = counts.max().round(2)
    min_count = counts.min().round(2)
    mean = counts.mean().round(2)
    std = counts.std().round(2)

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape()
    )
    template = env.get_template('README.j2')
    content = template.render(loto_result=loto_result, max_count=max_count, min_count=min_count, mean=mean, std=std, **small_results.iloc[-1])
    with open('README.md', 'w') as outfile:
        outfile.write(content)

    counts = counts.reset_index()
    counts.columns = ['value', 'freq']

    # Detail plot

    heatmap_data = counts.copy()
    heatmap_data['tens'] = heatmap_data['value'] // 10
    heatmap_data['ones'] = heatmap_data['value'] % 10
    heatmap_data = heatmap_data[['tens', 'ones', 'freq']]
    heatmap_data = heatmap_data.pivot(index='tens', columns='ones', values='freq')

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn', ax=ax)
    ax.set_title('Detail')
    fig.savefig('images/heatmap.jpg')

    # Top 10 plot

    bar_data = counts[:10].copy()
    bar_data['value'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    fig, ax = plt.subplots()
    palette = reversed(colors_from_values(bar_data['freq'], 'summer'))
    sns.barplot(bar_data, x='value', y='freq', palette=palette, ax=ax)
    for bar in ax.containers:
        ax.bar_label(bar, fmt='%d')
    ax.set_title('Top 10')
    fig.savefig('images/top-10.jpg')

    # Distribution

    data = counts[['freq']].copy()
    bins = data.max()[0] - data.min()[0] + 1

    fig, ax = plt.subplots()
    sns.histplot(data, kde=True, bins=bins, fill=False, ax=ax)
    kdeline = ax.lines[0]
    xs = kdeline.get_xdata()
    ys = kdeline.get_ydata()
    ax.vlines(mean, 0, np.interp(mean, xs, ys), color='red', linestyles='solid')
    ax.vlines(mean - std, 0, np.interp(mean - std, xs, ys), color='red', linestyles='dashed')
    ax.vlines(mean + std, 0, np.interp(mean + std, xs, ys), color='red', linestyles='dashed')
    ax.vlines(mean - 2*std, 0, np.interp(mean - 2*std, xs, ys), color='red', linestyles='dotted')
    ax.vlines(mean + 2*std, 0, np.interp(mean + 2*std, xs, ys), color='red', linestyles='dotted')
    ax.set_title('Distribution')
    fig.savefig('images/distribution.jpg')

    # Last appearing Loto
    last_appearing_loto(small_results)
