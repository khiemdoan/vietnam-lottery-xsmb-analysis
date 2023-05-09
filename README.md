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
| <table><tr><td>Date</td><td>09-05-2023</td></tr><tr><td>Special</td><td>58546</td></tr><tr><td>First</td><td>87138</td></tr><tr><td>Second</td><td>70752, 46168</td></tr><tr><td rowspan="2">Third</td><td>96208, 31488, 86067</td></tr><tr><td>22183, 37859, 54970</td></tr><tr><td>Fourth</td><td>5523, 1471, 7978, 9994</td></tr><tr><td rowspan="2">Fifth</td><td>2767, 1142, 9742</td></tr><tr><td>9327, 1226, 7965</td></tr><tr><td>Sixth</td><td>921, 554, 160</td></tr><tr><td>Seventh</td><td>30, 25, 64, 14</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>8</td></tr><tr><td>1</td><td>4</td></tr><tr><td>2</td><td>1, 3, 5, 6, 7</td></tr><tr><td>3</td><td>0, 8</td></tr><tr><td>4</td><td>2, 2, 6</td></tr><tr><td>5</td><td>2, 4, 9</td></tr><tr><td>6</td><td>0, 4, 5, 7, 7, 8</td></tr><tr><td>7</td><td>0, 1, 8</td></tr><tr><td>8</td><td>3, 8</td></tr><tr><td>9</td><td>4</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 74.

Mean: 97.47. Standard deviation: 10.42.

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