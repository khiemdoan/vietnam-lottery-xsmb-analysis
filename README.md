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
| <table><tr><td>Date</td><td>22-03-2024</td></tr><tr><td>Special</td><td>95371</td></tr><tr><td>First</td><td>07286</td></tr><tr><td>Second</td><td>23998, 54295</td></tr><tr><td rowspan="2">Third</td><td>30927, 81184, 68459</td></tr><tr><td>29360, 97671, 18598</td></tr><tr><td>Fourth</td><td>3721, 6102, 6363, 6756</td></tr><tr><td rowspan="2">Fifth</td><td>7582, 1471, 1256</td></tr><tr><td>7423, 3322, 6997</td></tr><tr><td>Sixth</td><td>840, 527, 579</td></tr><tr><td>Seventh</td><td>21, 91, 03, 69</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 3</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>1, 1, 2, 3, 7, 7</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>0</td></tr><tr><td>5</td><td>6, 6, 9</td></tr><tr><td>6</td><td>0, 3, 9</td></tr><tr><td>7</td><td>1, 1, 1, 9</td></tr><tr><td>8</td><td>2, 4, 6</td></tr><tr><td>9</td><td>1, 5, 7, 8, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 119. Min: 78.

Mean: 97.74. Standard deviation: 8.87.

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