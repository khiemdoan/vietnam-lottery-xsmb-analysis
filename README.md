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
| <table><tr><td>Date</td><td>16-04-2023</td></tr><tr><td>Special</td><td>41248</td></tr><tr><td>First</td><td>17827</td></tr><tr><td>Second</td><td>73986, 79480</td></tr><tr><td rowspan="2">Third</td><td>41224, 34610, 25369</td></tr><tr><td>86403, 80143, 57669</td></tr><tr><td>Fourth</td><td>1141, 3622, 2677, 0520</td></tr><tr><td rowspan="2">Fifth</td><td>1337, 5356, 2412</td></tr><tr><td>7235, 8435, 2100</td></tr><tr><td>Sixth</td><td>803, 944, 321</td></tr><tr><td>Seventh</td><td>26, 28, 70, 72</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 3, 3</td></tr><tr><td>1</td><td>0, 2</td></tr><tr><td>2</td><td>0, 1, 2, 4, 6, 7, 8</td></tr><tr><td>3</td><td>5, 5, 7</td></tr><tr><td>4</td><td>1, 3, 4, 8</td></tr><tr><td>5</td><td>6</td></tr><tr><td>6</td><td>9, 9</td></tr><tr><td>7</td><td>0, 2, 7</td></tr><tr><td>8</td><td>0, 6</td></tr><tr><td>9</td><td>-</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 73.

Mean: 97.47. Standard deviation: 10.94.

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