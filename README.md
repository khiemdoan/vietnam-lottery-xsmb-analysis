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
| <table><tr><td>Date</td><td>17-03-2024</td></tr><tr><td>Special</td><td>39399</td></tr><tr><td>First</td><td>50264</td></tr><tr><td>Second</td><td>05861, 93264</td></tr><tr><td rowspan="2">Third</td><td>27209, 38005, 89679</td></tr><tr><td>63829, 34307, 28483</td></tr><tr><td>Fourth</td><td>4711, 8630, 7059, 6601</td></tr><tr><td rowspan="2">Fifth</td><td>8554, 0583, 0657</td></tr><tr><td>3523, 3494, 1252</td></tr><tr><td>Sixth</td><td>639, 625, 190</td></tr><tr><td>Seventh</td><td>02, 50, 20, 30</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 2, 5, 7, 9</td></tr><tr><td>1</td><td>1</td></tr><tr><td>2</td><td>0, 3, 5, 9</td></tr><tr><td>3</td><td>0, 0, 9</td></tr><tr><td>4</td><td>-</td></tr><tr><td>5</td><td>0, 2, 4, 7, 9</td></tr><tr><td>6</td><td>1, 4, 4</td></tr><tr><td>7</td><td>9</td></tr><tr><td>8</td><td>3, 3</td></tr><tr><td>9</td><td>0, 4, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 79.

Mean: 97.74. Standard deviation: 8.83.

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