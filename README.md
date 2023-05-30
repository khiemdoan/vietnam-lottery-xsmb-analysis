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
| <table><tr><td>Date</td><td>30-05-2023</td></tr><tr><td>Special</td><td>20765</td></tr><tr><td>First</td><td>15037</td></tr><tr><td>Second</td><td>35868, 93065</td></tr><tr><td rowspan="2">Third</td><td>57840, 39646, 93650</td></tr><tr><td>76407, 80500, 27833</td></tr><tr><td>Fourth</td><td>7861, 9818, 7371, 0560</td></tr><tr><td rowspan="2">Fifth</td><td>7185, 0130, 9462</td></tr><tr><td>2951, 0104, 1993</td></tr><tr><td>Sixth</td><td>287, 387, 650</td></tr><tr><td>Seventh</td><td>96, 60, 37, 21</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 4, 7</td></tr><tr><td>1</td><td>8</td></tr><tr><td>2</td><td>1</td></tr><tr><td>3</td><td>0, 3, 7, 7</td></tr><tr><td>4</td><td>0, 6</td></tr><tr><td>5</td><td>0, 0, 1</td></tr><tr><td>6</td><td>0, 0, 1, 2, 5, 5, 8</td></tr><tr><td>7</td><td>1</td></tr><tr><td>8</td><td>5, 7, 7</td></tr><tr><td>9</td><td>3, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 121. Min: 74.

Mean: 97.47. Standard deviation: 10.53.

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