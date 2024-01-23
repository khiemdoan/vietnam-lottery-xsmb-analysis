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
| <table><tr><td>Date</td><td>23-01-2024</td></tr><tr><td>Special</td><td>87441</td></tr><tr><td>First</td><td>45966</td></tr><tr><td>Second</td><td>06221, 88252</td></tr><tr><td rowspan="2">Third</td><td>27745, 45816, 68217</td></tr><tr><td>41517, 41912, 32545</td></tr><tr><td>Fourth</td><td>7691, 4975, 9911, 6182</td></tr><tr><td rowspan="2">Fifth</td><td>6097, 1046, 6006</td></tr><tr><td>2575, 2298, 6725</td></tr><tr><td>Sixth</td><td>022, 468, 449</td></tr><tr><td>Seventh</td><td>74, 00, 49, 11</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 6</td></tr><tr><td>1</td><td>1, 1, 2, 6, 7, 7</td></tr><tr><td>2</td><td>1, 2, 5</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>1, 5, 5, 6, 9, 9</td></tr><tr><td>5</td><td>2</td></tr><tr><td>6</td><td>6, 8</td></tr><tr><td>7</td><td>4, 5, 5</td></tr><tr><td>8</td><td>2</td></tr><tr><td>9</td><td>1, 7, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 124. Min: 81.

Mean: 98.28. Standard deviation: 8.84.

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