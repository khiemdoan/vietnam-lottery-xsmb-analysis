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
| <table><tr><td>Date</td><td>17-09-2023</td></tr><tr><td>Special</td><td>22365</td></tr><tr><td>First</td><td>80585</td></tr><tr><td>Second</td><td>51233, 18206</td></tr><tr><td rowspan="2">Third</td><td>96019, 28041, 33335</td></tr><tr><td>84405, 47766, 56983</td></tr><tr><td>Fourth</td><td>0662, 9764, 3649, 9731</td></tr><tr><td rowspan="2">Fifth</td><td>9034, 3966, 3093</td></tr><tr><td>1775, 7898, 1925</td></tr><tr><td>Sixth</td><td>266, 316, 572</td></tr><tr><td>Seventh</td><td>97, 50, 53, 24</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>5, 6</td></tr><tr><td>1</td><td>6, 9</td></tr><tr><td>2</td><td>4, 5</td></tr><tr><td>3</td><td>1, 3, 4, 5</td></tr><tr><td>4</td><td>1, 9</td></tr><tr><td>5</td><td>0, 3</td></tr><tr><td>6</td><td>2, 4, 5, 6, 6, 6</td></tr><tr><td>7</td><td>2, 5</td></tr><tr><td>8</td><td>3, 5</td></tr><tr><td>9</td><td>3, 7, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 77.

Mean: 97.47. Standard deviation: 10.05.

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