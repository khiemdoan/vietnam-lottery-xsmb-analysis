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
| <table><tr><td>Date</td><td>19-02-2024</td></tr><tr><td>Special</td><td>75801</td></tr><tr><td>First</td><td>19995</td></tr><tr><td>Second</td><td>93219, 56742</td></tr><tr><td rowspan="2">Third</td><td>13459, 21260, 02582</td></tr><tr><td>01053, 92502, 27859</td></tr><tr><td>Fourth</td><td>1440, 1020, 4024, 9170</td></tr><tr><td rowspan="2">Fifth</td><td>0057, 6215, 3858</td></tr><tr><td>8144, 3559, 8224</td></tr><tr><td>Sixth</td><td>554, 331, 982</td></tr><tr><td>Seventh</td><td>64, 85, 24, 66</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 2</td></tr><tr><td>1</td><td>5, 9</td></tr><tr><td>2</td><td>0, 4, 4, 4</td></tr><tr><td>3</td><td>1</td></tr><tr><td>4</td><td>0, 2, 4</td></tr><tr><td>5</td><td>3, 4, 7, 8, 9, 9, 9</td></tr><tr><td>6</td><td>0, 4, 6</td></tr><tr><td>7</td><td>0</td></tr><tr><td>8</td><td>2, 2, 5</td></tr><tr><td>9</td><td>5</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 80.

Mean: 97.47. Standard deviation: 8.72.

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