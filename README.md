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
| <table><tr><td>Date</td><td>06-04-2024</td></tr><tr><td>Special</td><td>00312</td></tr><tr><td>First</td><td>44708</td></tr><tr><td>Second</td><td>88283, 64571</td></tr><tr><td rowspan="2">Third</td><td>91798, 21146, 05250</td></tr><tr><td>09523, 92549, 73943</td></tr><tr><td>Fourth</td><td>1449, 2399, 7871, 7371</td></tr><tr><td rowspan="2">Fifth</td><td>5848, 3389, 9405</td></tr><tr><td>8301, 7420, 2661</td></tr><tr><td>Sixth</td><td>142, 732, 198</td></tr><tr><td>Seventh</td><td>21, 59, 95, 03</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 3, 5, 8</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>0, 1, 3</td></tr><tr><td>3</td><td>2</td></tr><tr><td>4</td><td>2, 3, 6, 8, 9, 9</td></tr><tr><td>5</td><td>0, 9</td></tr><tr><td>6</td><td>1</td></tr><tr><td>7</td><td>1, 1, 1</td></tr><tr><td>8</td><td>3, 9</td></tr><tr><td>9</td><td>5, 8, 8, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 72.

Mean: 97.74. Standard deviation: 9.15.

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