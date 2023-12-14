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
| <table><tr><td>Date</td><td>14-12-2023</td></tr><tr><td>Special</td><td>06245</td></tr><tr><td>First</td><td>38517</td></tr><tr><td>Second</td><td>40644, 70647</td></tr><tr><td rowspan="2">Third</td><td>81520, 69703, 11751</td></tr><tr><td>71184, 82277, 25595</td></tr><tr><td>Fourth</td><td>7806, 3861, 3836, 2974</td></tr><tr><td rowspan="2">Fifth</td><td>8284, 0885, 1003</td></tr><tr><td>4565, 1675, 1006</td></tr><tr><td>Sixth</td><td>364, 482, 020</td></tr><tr><td>Seventh</td><td>15, 86, 76, 49</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>3, 3, 6, 6</td></tr><tr><td>1</td><td>5, 7</td></tr><tr><td>2</td><td>0, 0</td></tr><tr><td>3</td><td>6</td></tr><tr><td>4</td><td>4, 5, 7, 9</td></tr><tr><td>5</td><td>1</td></tr><tr><td>6</td><td>1, 4, 5</td></tr><tr><td>7</td><td>4, 5, 6, 7</td></tr><tr><td>8</td><td>2, 4, 4, 5, 6</td></tr><tr><td>9</td><td>5</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 128. Min: 78.

Mean: 97.47. Standard deviation: 9.31.

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