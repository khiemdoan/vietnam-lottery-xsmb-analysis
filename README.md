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
| <table><tr><td>Date</td><td>19-12-2023</td></tr><tr><td>Special</td><td>14577</td></tr><tr><td>First</td><td>66388</td></tr><tr><td>Second</td><td>72506, 57508</td></tr><tr><td rowspan="2">Third</td><td>00305, 65882, 84801</td></tr><tr><td>38647, 30901, 12566</td></tr><tr><td>Fourth</td><td>2019, 7061, 7062, 9014</td></tr><tr><td rowspan="2">Fifth</td><td>1202, 5718, 9539</td></tr><tr><td>9204, 5379, 0370</td></tr><tr><td>Sixth</td><td>308, 532, 193</td></tr><tr><td>Seventh</td><td>40, 82, 90, 57</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 1, 2, 4, 5, 6, 8, 8</td></tr><tr><td>1</td><td>4, 8, 9</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>2, 9</td></tr><tr><td>4</td><td>0, 7</td></tr><tr><td>5</td><td>7</td></tr><tr><td>6</td><td>1, 2, 6</td></tr><tr><td>7</td><td>0, 7, 9</td></tr><tr><td>8</td><td>2, 2, 8</td></tr><tr><td>9</td><td>0, 3</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 129. Min: 78.

Mean: 97.47. Standard deviation: 9.31.

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