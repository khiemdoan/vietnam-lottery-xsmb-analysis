__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from pandera.pandas import Check, Column, DataFrameSchema

from dtos import Result

PRIZE_COLUMNS = [name for name in Result.model_fields if name != 'date']
NUMBER_OF_PRIZES = len(PRIZE_COLUMNS)

DATE_COLUMN = Column('datetime64[ns]', unique=True, nullable=False)

RAW_SCHEMA = DataFrameSchema(
    {
        'date': DATE_COLUMN,
        **{name: Column('int64', checks=[Check.ge(0), Check.le(99_999)], nullable=False) for name in PRIZE_COLUMNS},
    },
    strict=True,
)

TWO_DIGITS_SCHEMA = DataFrameSchema(
    {
        'date': DATE_COLUMN,
        **{name: Column('int64', checks=Check.in_range(0, 99), nullable=False) for name in PRIZE_COLUMNS},
    },
    strict=True,
)

SPARSE_SCHEMA = DataFrameSchema(
    {
        'date': DATE_COLUMN,
        **{f'{i:02d}': Column('int64', checks=Check.ge(0), nullable=False) for i in range(100)},
    },
    checks=Check(
        lambda df: df.drop(columns='date').sum(axis=1).eq(NUMBER_OF_PRIZES).all(),
        error=f'each row must contain exactly {NUMBER_OF_PRIZES} numbers',
    ),
    strict=True,
)
