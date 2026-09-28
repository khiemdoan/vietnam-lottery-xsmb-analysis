__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from datetime import date

from crawler import Crawler


def test_crawler() -> None:
    with Crawler() as crawler:
        result = crawler.fetch(date(2026, 1, 1))
    assert result is not None
