# Vietnam Lottery (XSMB) Analysis

Using GitHub Action to automatically fetch and analyze results of the Vietnam lottery daily.

Download:

* [Full data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb.csv)
* [1-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_1_year.csv)
* [2-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_2_year.csv)
* [3-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_3_year.csv)
* [5-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_5_year.csv)

| Lotery      | Loto |
| :-----------: | :-----------: |
| <table><tr><td>Date</td><td>01-01-2024</td></tr><tr><td>Special</td><td>42932</td></tr><tr><td>First</td><td>66272</td></tr><tr><td>Second</td><td>27370, 68541</td></tr><tr><td rowspan="2">Third</td><td>55788, 04997, 82222</td></tr><tr><td>02980, 83746, 18098</td></tr><tr><td>Fourth</td><td>5667, 8086, 5934, 0473</td></tr><tr><td rowspan="2">Fifth</td><td>1851, 1006, 0384</td></tr><tr><td>6131, 8065, 5365</td></tr><tr><td>Sixth</td><td>255, 166, 353</td></tr><tr><td>Seventh</td><td>53, 73, 45, 79</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>6</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>2</td></tr><tr><td>3</td><td>1, 2, 4</td></tr><tr><td>4</td><td>1, 5, 6</td></tr><tr><td>5</td><td>1, 3, 3, 5</td></tr><tr><td>6</td><td>5, 5, 6, 7</td></tr><tr><td>7</td><td>0, 2, 3, 3, 9</td></tr><tr><td>8</td><td>0, 4, 6, 8</td></tr><tr><td>9</td><td>7, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 128. Min: 79.

Mean: 97.47. Standard deviation: 9.44.

<h3>Detail</h3>

![Detail](images/heatmap.jpg)

<h3>Top 10</h3>

![Top 10](images/top-10.jpg)

<h3>Distribution</h3>

![Distribution](images/distribution.jpg)

<h2>Amount of day from last appearing</h2>

![Delta](images/delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/delta_top_10.jpg)