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
| <table><tr><td>Date</td><td>22-10-2023</td></tr><tr><td>Special</td><td>91918</td></tr><tr><td>First</td><td>71417</td></tr><tr><td>Second</td><td>88769, 04327</td></tr><tr><td rowspan="2">Third</td><td>51414, 00736, 72340</td></tr><tr><td>97988, 72175, 71832</td></tr><tr><td>Fourth</td><td>6133, 5179, 2610, 9379</td></tr><tr><td rowspan="2">Fifth</td><td>5776, 3154, 1993</td></tr><tr><td>8030, 4721, 1483</td></tr><tr><td>Sixth</td><td>740, 282, 296</td></tr><tr><td>Seventh</td><td>92, 25, 24, 11</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>0, 1, 4, 7, 8</td></tr><tr><td>2</td><td>1, 4, 5, 7</td></tr><tr><td>3</td><td>0, 2, 3, 6</td></tr><tr><td>4</td><td>0, 0</td></tr><tr><td>5</td><td>4</td></tr><tr><td>6</td><td>9</td></tr><tr><td>7</td><td>5, 6, 9, 9</td></tr><tr><td>8</td><td>2, 3, 8</td></tr><tr><td>9</td><td>2, 3, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 127. Min: 75.

Mean: 97.47. Standard deviation: 9.48.

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