__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from contextlib import AbstractContextManager
from datetime import date
from typing import Self

from bs4 import BeautifulSoup
from cloudscraper import CloudScraper
from tenacity import retry, retry_if_not_exception_type, stop_after_attempt, wait_exponential

from dtos import Result

REQUEST_TIMEOUT = 30
PRIZE_COUNTS = frozendict({
    'special-prize': 1,
    'prize1': 1,
    'prize2': 2,
    'prize3': 6,
    'prize4': 4,
    'prize5': 6,
    'prize6': 3,
    'prize7': 4,
})


class Crawler(AbstractContextManager['Crawler']):
    def __enter__(self) -> Self:
        self._http: CloudScraper = CloudScraper()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._http.close()

    @staticmethod
    def _extract_prizes(soup: BeautifulSoup, css_class: str) -> list[int]:
        return [int(node.get_text(strip=True)) for node in soup.find_all(class_=css_class)]

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(min=1, max=10),
        retry=retry_if_not_exception_type(ValueError),
    )
    def fetch(self, selected_date: date) -> Result | None:
        url = f'https://xoso.com.vn/xsmb-{selected_date:%d-%m-%Y}.html'
        resp = self._http.get(url, timeout=REQUEST_TIMEOUT)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, 'lxml')
        prizes = {css_class: self._extract_prizes(soup, css_class) for css_class in PRIZE_COUNTS}

        if not any(prizes.values()):
            return None

        for css_class, values in prizes.items():
            expected = PRIZE_COUNTS[css_class]
            if len(values) != expected:
                raise ValueError(f'Expected {expected} {css_class} prizes, got {len(values)}')

        special = prizes['special-prize']
        prize1 = prizes['prize1']
        prize2 = prizes['prize2']
        prize3 = prizes['prize3']
        prize4 = prizes['prize4']
        prize5 = prizes['prize5']
        prize6 = prizes['prize6']
        prize7 = prizes['prize7']

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
