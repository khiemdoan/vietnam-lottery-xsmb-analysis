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
| <table><tr><td>Date</td><td>09-04-2024</td></tr><tr><td>Special</td><td>16510</td></tr><tr><td>First</td><td>57524</td></tr><tr><td>Second</td><td>46210, 99866</td></tr><tr><td rowspan="2">Third</td><td>59326, 97595, 41257</td></tr><tr><td>02724, 00969, 52074</td></tr><tr><td>Fourth</td><td>0760, 1668, 3313, 3684</td></tr><tr><td rowspan="2">Fifth</td><td>6299, 7898, 4768</td></tr><tr><td>6210, 3355, 4816</td></tr><tr><td>Sixth</td><td>717, 130, 568</td></tr><tr><td>Seventh</td><td>69, 62, 27, 41</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>0, 0, 0, 3, 6, 7</td></tr><tr><td>2</td><td>4, 4, 6, 7</td></tr><tr><td>3</td><td>0</td></tr><tr><td>4</td><td>1</td></tr><tr><td>5</td><td>5, 7</td></tr><tr><td>6</td><td>0, 2, 6, 8, 8, 8, 9, 9</td></tr><tr><td>7</td><td>4</td></tr><tr><td>8</td><td>4</td></tr><tr><td>9</td><td>5, 8, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 73.

Mean: 97.74. Standard deviation: 9.36.

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