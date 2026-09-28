__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from contextlib import AbstractContextManager
from datetime import date
from typing import Self

from bs4 import BeautifulSoup
from cloudscraper import CloudScraper
from tenacity import retry, stop_after_attempt, wait_exponential

from dtos import Result


class Crawler(AbstractContextManager):
    def __enter__(self) -> Self:
        self._http = CloudScraper()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._http.close()

    @retry(stop=stop_after_attempt(5), wait=wait_exponential(min=1, max=10))
    def fetch(self, selected_date: date) -> Result:
        url = f'https://xoso.com.vn/xsmb-{selected_date:%d-%m-%Y}.html'
        resp = self._http.get(url)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, 'lxml')
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

        if len(special) == 0:
            return

        return Result(
            date=selected_date,
            special=special[0],
            prize1=prize1[0],
            prize2_1=prize2[0],
            prize2_2=prize2[1],
            prize3_1=prize3[0],
            prize3_2=prize3[1],
            prize3_3=prize3[2],
            prize3_4=prize3[3],
            prize3_5=prize3[4],
            prize3_6=prize3[5],
            prize4_1=prize4[0],
            prize4_2=prize4[1],
            prize4_3=prize4[2],
            prize4_4=prize4[3],
            prize5_1=prize5[0],
            prize5_2=prize5[1],
            prize5_3=prize5[2],
            prize5_4=prize5[3],
            prize5_5=prize5[4],
            prize5_6=prize5[5],
            prize6_1=prize6[0],
            prize6_2=prize6[1],
            prize6_3=prize6[2],
            prize7_1=prize7[0],
            prize7_2=prize7[1],
            prize7_3=prize7[2],
            prize7_4=prize7[3],
        )
