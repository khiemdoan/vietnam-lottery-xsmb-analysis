__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

from crawler import Crawler
from lottery import Lottery

if __name__ == '__main__':
    lottery = Lottery()
    lottery.load()

    # Download new data

    begin_date = lottery.get_last_date()
    tz = ZoneInfo('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)
    last_date = now.date()
    if now.time() < time(18, 35):
        last_date -= timedelta(days=1)

    delta = (last_date - begin_date).days + 1
    with Crawler() as crawler:
        for i in range(1, delta):
            try:
                selected_date = begin_date + timedelta(days=i)
                print(f'Fetching: {selected_date}')
                result = crawler.fetch(selected_date)
                lottery.update(result)
            except Exception as e:
                print(f'Error fetching data for {selected_date}: {e}')

    lottery.generate_dataframes()
    lottery.dump()
