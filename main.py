
__author__ = 'KhiemDH'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

import itertools
from dataclasses import asdict, dataclass
from datetime import date, datetime, time, timedelta
from time import sleep
from typing import Dict, List

import pandas as pd
from bs4 import BeautifulSoup
from cloudscraper import CloudScraper
from pytz import timezone


@dataclass
class Result:
    date: date
    special: List[int]
    prize1: List[int]
    prize2: List[int]
    prize3: List[int]
    prize4: List[int]
    prize5: List[int]
    prize6: List[int]
    prize7: List[int]


def fetch_result(selected_date: date) -> Result:
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
    result = Result(selected_date, special, prize1, prize2, prize3, prize4, prize5, prize6, prize7)
    return result


def convert_result_to_series(result: Result) -> Dict:
    data = {}
    for key, value in asdict(result).items():
        if key == 'date':
            data['date'] = value
        elif len(value) == 1:
            data[key] = value[0]
        else:
            for i, v in enumerate(value, start=1):
                data[f'{key}-{i}'] = v
    series = pd.Series(data)
    return series


if __name__ == '__main__':
    tz = timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)

    start_date = date(2010, 1, 1)
    last_date = now.date()
    if now.time() < time(18, 35):
        last_date -= timedelta(days=1)

    results: List[Result] = []
    result_series: List[pd.Series] = []

    delta = (last_date - start_date).days + 1
    for i in range(delta):
        selected_date = start_date + timedelta(days=i)
        result = fetch_result(selected_date)
        print(result)
        sleep(0.1)
        if len(result.special) == 0:
            continue
        series = convert_result_to_series(result)
        result_series.append(series)

    g = itertools.groupby(len(r.special) for r in results)
    assert next(g, True) and not next(g, False)
    g = itertools.groupby(len(r.prize1) for r in results)
    assert next(g, True) and not next(g, False)
    g = itertools.groupby(len(r.prize2) for r in results)
    assert next(g, True) and not next(g, False)
    g = itertools.groupby(len(r.prize3) for r in results)
    assert next(g, True) and not next(g, False)
    g = itertools.groupby(len(r.prize4) for r in results)
    assert next(g, True) and not next(g, False)
    g = itertools.groupby(len(r.prize5) for r in results)
    assert next(g, True) and not next(g, False)
    g = itertools.groupby(len(r.prize6) for r in results)
    assert next(g, True) and not next(g, False)
    g = itertools.groupby(len(r.prize7) for r in results)
    assert next(g, True) and not next(g, False)

    df = pd.DataFrame(result_series)
    df.set_index('date', inplace=True)
    df.to_csv('results/xsmb.csv')
