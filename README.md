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
| <table><tr><td>Date</td><td>24-02-2024</td></tr><tr><td>Special</td><td>57333</td></tr><tr><td>First</td><td>81369</td></tr><tr><td>Second</td><td>30504, 76199</td></tr><tr><td rowspan="2">Third</td><td>33651, 22945, 66456</td></tr><tr><td>46182, 39290, 34970</td></tr><tr><td>Fourth</td><td>7837, 6860, 3636, 6890</td></tr><tr><td rowspan="2">Fifth</td><td>1619, 7224, 1740</td></tr><tr><td>4222, 1496, 0442</td></tr><tr><td>Sixth</td><td>247, 752, 331</td></tr><tr><td>Seventh</td><td>43, 44, 35, 45</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>4</td></tr><tr><td>1</td><td>9</td></tr><tr><td>2</td><td>2, 4</td></tr><tr><td>3</td><td>1, 3, 5, 6, 7</td></tr><tr><td>4</td><td>0, 2, 3, 4, 5, 5, 7</td></tr><tr><td>5</td><td>1, 2, 6</td></tr><tr><td>6</td><td>0, 9</td></tr><tr><td>7</td><td>0</td></tr><tr><td>8</td><td>2</td></tr><tr><td>9</td><td>0, 0, 6, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 77.

Mean: 97.47. Standard deviation: 8.6.

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