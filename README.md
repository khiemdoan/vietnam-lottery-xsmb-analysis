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
| <table><tr><td>Date</td><td>10-04-2024</td></tr><tr><td>Special</td><td>14138</td></tr><tr><td>First</td><td>62724</td></tr><tr><td>Second</td><td>54157, 96213</td></tr><tr><td rowspan="2">Third</td><td>14362, 89770, 55669</td></tr><tr><td>50544, 04462, 48939</td></tr><tr><td>Fourth</td><td>4062, 5079, 6608, 7155</td></tr><tr><td rowspan="2">Fifth</td><td>7402, 1236, 4922</td></tr><tr><td>4421, 2178, 9253</td></tr><tr><td>Sixth</td><td>552, 247, 722</td></tr><tr><td>Seventh</td><td>12, 45, 75, 97</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 8</td></tr><tr><td>1</td><td>2, 3</td></tr><tr><td>2</td><td>1, 2, 2, 4</td></tr><tr><td>3</td><td>6, 8, 9</td></tr><tr><td>4</td><td>4, 5, 7</td></tr><tr><td>5</td><td>2, 3, 5, 7</td></tr><tr><td>6</td><td>2, 2, 2, 9</td></tr><tr><td>7</td><td>0, 5, 8, 9</td></tr><tr><td>8</td><td>-</td></tr><tr><td>9</td><td>7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 127. Min: 73.

Mean: 97.74. Standard deviation: 9.41.

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