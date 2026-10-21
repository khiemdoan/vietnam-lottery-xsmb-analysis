__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from datetime import date

import pytest
from pandera.errors import SchemaErrors

from dtos import Result
from lottery import Lottery


def create_lottery() -> Lottery:
    result = Result(date=date(2026, 1, 1), **{name: 0 for name in Result.model_fields if name != 'date'})

    lottery = Lottery()
    lottery.update(result)
    lottery.generate_dataframes()
    return lottery


def test_sparse_data_columns() -> None:
    sparse_data = create_lottery().get_sparse_data()

    assert sparse_data.columns.tolist() == ['date', *[f'{i:02d}' for i in range(100)]]
    assert sparse_data['00'].iloc[0] == len(Result.model_fields) - 1


def test_validate_accepts_generated_data() -> None:
    create_lottery().validate()


def test_validate_rejects_negative_prize() -> None:
    lottery = create_lottery()
    lottery.get_raw_data().loc[0, 'special'] = -1

    with pytest.raises(SchemaErrors):
        lottery.validate()


def test_validate_rejects_out_of_range_two_digits() -> None:
    lottery = create_lottery()
    lottery.get_2_digits_data().loc[0, 'special'] = 100

    with pytest.raises(SchemaErrors):
        lottery.validate()


def test_validate_rejects_incomplete_sparse_row() -> None:
    lottery = create_lottery()
    lottery.get_sparse_data().loc[0, '00'] = 0

    with pytest.raises(SchemaErrors):
        lottery.validate()
