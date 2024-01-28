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
| <table><tr><td>Date</td><td>28-01-2024</td></tr><tr><td>Special</td><td>68274</td></tr><tr><td>First</td><td>93911</td></tr><tr><td>Second</td><td>25484, 47616</td></tr><tr><td rowspan="2">Third</td><td>11003, 93986, 15302</td></tr><tr><td>61278, 13916, 23900</td></tr><tr><td>Fourth</td><td>1710, 1445, 4678, 9751</td></tr><tr><td rowspan="2">Fifth</td><td>5496, 0228, 3343</td></tr><tr><td>5479, 4126, 8089</td></tr><tr><td>Sixth</td><td>221, 438, 853</td></tr><tr><td>Seventh</td><td>87, 65, 49, 41</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 2, 3</td></tr><tr><td>1</td><td>0, 1, 6, 6</td></tr><tr><td>2</td><td>1, 6, 8</td></tr><tr><td>3</td><td>8</td></tr><tr><td>4</td><td>1, 3, 5, 9</td></tr><tr><td>5</td><td>1, 3</td></tr><tr><td>6</td><td>5</td></tr><tr><td>7</td><td>4, 8, 8, 9</td></tr><tr><td>8</td><td>4, 6, 7, 9</td></tr><tr><td>9</td><td>6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 127. Min: 81.

Mean: 98.55. Standard deviation: 8.93.

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