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
| <table><tr><td>Date</td><td>20-08-2023</td></tr><tr><td>Special</td><td>92009</td></tr><tr><td>First</td><td>83433</td></tr><tr><td>Second</td><td>73249, 22498</td></tr><tr><td rowspan="2">Third</td><td>88300, 82515, 35780</td></tr><tr><td>46685, 15696, 01620</td></tr><tr><td>Fourth</td><td>4914, 8375, 3112, 7130</td></tr><tr><td rowspan="2">Fifth</td><td>1530, 2557, 5432</td></tr><tr><td>3299, 4793, 9846</td></tr><tr><td>Sixth</td><td>745, 471, 190</td></tr><tr><td>Seventh</td><td>61, 79, 95, 58</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 9</td></tr><tr><td>1</td><td>2, 4, 5</td></tr><tr><td>2</td><td>0</td></tr><tr><td>3</td><td>0, 0, 2, 3</td></tr><tr><td>4</td><td>5, 6, 9</td></tr><tr><td>5</td><td>7, 8</td></tr><tr><td>6</td><td>1</td></tr><tr><td>7</td><td>1, 5, 9</td></tr><tr><td>8</td><td>0, 5</td></tr><tr><td>9</td><td>0, 3, 5, 6, 8, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 77.

Mean: 97.47. Standard deviation: 10.22.

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