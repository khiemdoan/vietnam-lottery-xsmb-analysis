__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from copy import copy
from datetime import date

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from cloudscraper import CloudScraper

from src.dtos import Result, ResultList


class Lottery:
    def __init__(self) -> None:
        self._http = CloudScraper()

        self._data: dict[date, Result] = {}

        self._raw_data: pd.DataFrame = pd.DataFrame()
        self._2_digits_data: pd.DataFrame = pd.DataFrame()
        self._sparse_data: pd.DataFrame = pd.DataFrame()

        self._begin_date = date.today()
        self._last_date = date.today()

    def load(self) -> None:
        with open('data/xsmb.json', 'r', encoding='utf-8') as f:
            data = ResultList.model_validate_json(f.read())
        for d in data.root:
            self._data[d.date] = d

    def dump(self) -> None:
        self._raw_data.to_csv('data/xsmb.csv', index=False)
        self._raw_data.to_json('data/xsmb.json', orient='records', date_format='iso', indent=2, index=False)

        self._2_digits_data.to_csv('data/xsmb-2-digits.csv', index=False)
        self._2_digits_data.to_json('data/xsmb-2-digits.json', orient='records', date_format='iso', indent=2, index=False)

        self._sparse_data.to_csv('data/xsmb-sparse.csv', index=False)
        self._sparse_data.to_json('data/xsmb-sparse.json', orient='records', date_format='iso', indent=2, index=False)

    def fetch(self, selected_date: date) -> None:
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

        result = Result(
            date=selected_date,
            special=special[0],
            prize1=prize1[0],
            prize2_1=prize2[0], prize2_2=prize2[1],
            prize3_1=prize3[0], prize3_2=prize3[1], prize3_3=prize3[2], prize3_4=prize3[3], prize3_5=prize3[4], prize3_6=prize3[5],
            prize4_1=prize4[0], prize4_2=prize4[1], prize4_3=prize4[2], prize4_4=prize4[3],
            prize5_1=prize5[0], prize5_2=prize5[1], prize5_3=prize5[2], prize5_4=prize5[3], prize5_5=prize5[4], prize5_6=prize5[5],
            prize6_1=prize6[0], prize6_2=prize6[1], prize6_3=prize6[2],
            prize7_1=prize7[0], prize7_2=prize7[1], prize7_3=prize7[2], prize7_4=prize7[3],
        )
        self._data[result.date] = result

    def generate_dataframes(self) -> None:
        self._raw_data = pd.DataFrame([d.model_dump() for d in self._data.values()])
        self._raw_data['date'] = pd.to_datetime(self._raw_data['date'])
        self._raw_data.iloc[:, 1:] = self._raw_data.iloc[:, 1:].astype('int64')

        self._2_digits_data = copy(self._raw_data)
        self._2_digits_data.iloc[:, 1:] = self._2_digits_data.iloc[:, 1:].apply(lambda x: x % 100)

        self._sparse_data = pd.concat(
            [
                self._2_digits_data.iloc[:, 0:1],
                pd.DataFrame(np.zeros((self._2_digits_data.shape[0], 100), dtype=int)),
            ],
            axis=1,
        )
        self._sparse_data.iloc[:, 1:] = self._sparse_data.iloc[:, 1:].astype('int64')
        for i in range(self._2_digits_data.shape[0]):
            counts = self._2_digits_data.iloc[i, 1:].value_counts()
            for k, v in counts.items():
                self._sparse_data.iloc[i, k + 1] = int(v)

        begin_date = self._raw_data['date'].min()
        self._begin_date = begin_date.to_pydatetime().date()
        last_date = self._raw_data['date'].max()
        self._last_date = last_date.to_pydatetime().date()

    def get_raw_data(self) -> pd.DataFrame:
        return self._raw_data

    def get_2_digits_data(self) -> pd.DataFrame:
        return self._2_digits_data

    def get_sparse_data(self) -> pd.DataFrame:
        return self._sparse_data

    def get_last_date(self) -> date:
        return self._last_date
