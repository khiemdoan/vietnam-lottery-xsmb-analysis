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
from jinja2 import Environment, FileSystemLoader, select_autoescape
from matplotlib import pyplot as plt
from pytz import timezone

from src.lottery import Lottery


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
    heatmap_data = heatmap_data.pivot(index='tens', columns='ones', values='delta').fillna(0)
    heatmap_data = heatmap_data.astype(int)

    bar_data = last_appearing.sort_values('delta', ascending=False)
    bar_data = bar_data.iloc[:10, :]
    bar_data.reset_index(inplace=True)
    bar_data = bar_data.rename(columns={'index': 'value'})
    bar_data['value'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn', ax=ax)
    ax.set_title('Delta')
    fig.savefig('images/special_delta.jpg')

    fig, ax = plt.subplots()
    palette = reversed(colors_from_values(bar_data['delta'], 'summer'))
    sns.barplot(bar_data, x='value', y='delta', hue='value', palette=palette, ax=ax)
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
    heatmap_data = heatmap_data.pivot(index='tens', columns='ones', values='delta').fillna(0)
    heatmap_data = heatmap_data.astype(int)

    bar_data = last_appearing.sort_values('delta', ascending=False)
    bar_data = bar_data.iloc[:10, :]
    bar_data.reset_index(inplace=True)
    bar_data = bar_data.rename(columns={'index': 'value'})
    bar_data['value'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn', ax=ax)
    ax.set_title('Delta')
    fig.savefig('images/delta.jpg')

    fig, ax = plt.subplots()
    palette = reversed(colors_from_values(bar_data['delta'], 'summer'))
    sns.barplot(bar_data, x='value', y='delta', hue='value', palette=palette, ax=ax)
    for bar in ax.containers:
        ax.bar_label(bar, fmt='%d')
    ax.set_title('Top 10')
    fig.savefig('images/delta_top_10.jpg')


if __name__ == '__main__':
    pd.options.io.parquet.engine = 'pyarrow'
    pd.options.mode.string_storage = 'pyarrow'

    lottery = Lottery()
    lottery.load()

    # Download new data

    begin_date = lottery.get_last_date()
    tz = timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)
    last_date = now.date()
    if now.time() < time(18, 35):
        last_date -= timedelta(days=1)

    delta = (last_date - begin_date).days + 1
    for i in range(1, delta):
        selected_date = begin_date + timedelta(days=i)
        print(f'Fetching: {selected_date}')
        lottery.fetch(selected_date)

    lottery.generate_dataframes()
    lottery.dump()

    # Analysis

    results = lottery.get_raw_data()
    sparse_results = lottery.get_sparse_data()

    last_date = results['date'].max()

    start_date = pd.Timestamp(year=last_date.year - 2, month=last_date.month, day=last_date.day)
    results_2_year = results[(start_date < results['date']) & (results['date'] <= last_date)]
    results_2_year.reset_index(drop=True, inplace=True)

    start_date = pd.Timestamp(year=last_date.year - 1, month=last_date.month, day=last_date.day)
    small_results = results[(start_date < results['date']) & (results['date'] <= last_date)]
    small_results.reset_index(drop=True, inplace=True)

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

    last_date = sparse_results['date'].max()

    start_date = pd.Timestamp(year=last_date.year - 1, month=last_date.month, day=last_date.day)
    sparse_results_1_year = sparse_results[
        (start_date < sparse_results['date']) & (sparse_results['date'] <= last_date)
    ]
    sparse_results_1_year.reset_index(drop=True, inplace=True)

    sparse_results_1_year = sparse_results_1_year.drop(columns=['date'])
    counts = sparse_results_1_year.sum(axis=0)

    max_count = counts.max().round(2)
    min_count = counts.min().round(2)
    mean = counts.mean().round(2)
    std = counts.std().round(2)

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(),
    )
    template = env.get_template('README.j2')
    content = template.render(
        loto_result=loto_result, max_count=max_count, min_count=min_count, mean=mean, std=std, **small_results.iloc[-1]
    )
    with open('README.md', 'w', encoding='utf-8') as outfile:
        outfile.write(content)

    counts = counts.reset_index()
    counts.columns = ['value', 'freq']
    counts = counts.astype({'value': int})
    counts.sort_values('freq', ascending=False, inplace=True)

    # Detail plot

    heatmap_data = counts.copy()
    heatmap_data['tens'] = heatmap_data['value'] // 10
    heatmap_data['ones'] = heatmap_data['value'] % 10
    heatmap_data = heatmap_data[['tens', 'ones', 'freq']]
    heatmap_data = heatmap_data.pivot(index='tens', columns='ones', values='freq').fillna(0)
    heatmap_data = heatmap_data.astype(int)

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn', ax=ax)
    ax.set_title('Detail')
    fig.savefig('images/heatmap.jpg')

    # Top 10 plot

    bar_data = counts[:10].copy()
    bar_data['value'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    fig, ax = plt.subplots()
    palette = reversed(colors_from_values(bar_data['freq'], 'summer'))
    sns.barplot(bar_data, x='value', y='freq', hue='value', palette=palette, ax=ax)
    for bar in ax.containers:
        ax.bar_label(bar, fmt='%d')
    ax.set_title('Top 10')
    fig.savefig('images/top-10.jpg')

    # Distribution

    data = counts[['freq']].copy()
    bins = data.max().iloc[0] - data.min().iloc[0] + 1

    fig, ax = plt.subplots()
    sns.histplot(data, kde=True, bins=bins, fill=False, ax=ax)
    kdeline = ax.lines[0]
    xs = kdeline.get_xdata()
    ys = kdeline.get_ydata()
    ax.vlines(mean, 0, np.interp(mean, xs, ys), color='red', linestyles='solid')
    ax.vlines(mean - std, 0, np.interp(mean - std, xs, ys), color='red', linestyles='dashed')
    ax.vlines(mean + std, 0, np.interp(mean + std, xs, ys), color='red', linestyles='dashed')
    ax.vlines(mean - 2 * std, 0, np.interp(mean - 2 * std, xs, ys), color='red', linestyles='dotted')
    ax.vlines(mean + 2 * std, 0, np.interp(mean + 2 * std, xs, ys), color='red', linestyles='dotted')
    ax.set_title('Distribution')
    fig.savefig('images/distribution.jpg')

    # Last appearing Loto
    last_appearing_loto(small_results)
