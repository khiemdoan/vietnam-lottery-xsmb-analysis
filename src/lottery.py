__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from datetime import date
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup
from cloudscraper import CloudScraper


class Lottery:
    def __init__(self) -> None:
        self._http = CloudScraper()

    def fetch(self, selected_date: date) -> pd.DataFrame:
        url = f'https://xoso.com.vn/xsmb-{selected_date:%d-%m-%Y}.html'
        response = self._http.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
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

    def load(self, path: Path) -> pd.DataFrame:
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
