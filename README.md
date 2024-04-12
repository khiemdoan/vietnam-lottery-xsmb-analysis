# Vietnam Lottery (XSMB) Analysis

Using GitHub Action to automatically fetch and analyze results of the Vietnam lottery daily.

Download:

* [Full data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb.csv)
* [1-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_1_year.csv)
* [2-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_2_year.csv)
* [3-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_3_year.csv)
* [5-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_5_year.csv)

| Lotery (Xổ số) | Loto (Lô tô) |
| :------------: | :----------: |
| <table><tr><td>Date (Ngày)</td><td>12-04-2024</td></tr><tr><td>Special (Giải dặc biệt)</td><td>12073</td></tr><tr><td>First (Giải nhất)</td><td>92837</td></tr><tr><td>Second (Giải nhì)</td><td>28622, 02259</td></tr><tr><td rowspan="2">Third (Giải ba)</td><td>53010, 14391, 79427</td></tr><tr><td>13247, 76972, 60599</td></tr><tr><td>Fourth (Giải tư)</td><td>6594, 5821, 6858, 2983</td></tr><tr><td rowspan="2">Fifth (Giải năm)</td><td>0993, 5483, 8027</td></tr><tr><td>6916, 5213, 4770</td></tr><tr><td>Sixth (Giải sáu)</td><td>850, 036, 185</td></tr><tr><td>Seventh (Giải bảy)</td><td>27, 83, 16, 80</td></tr></table> | <table><tr><td>First (Đầu)</td><td>Last (Đuôi)</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>0, 3, 6, 6</td></tr><tr><td>2</td><td>1, 2, 7, 7, 7</td></tr><tr><td>3</td><td>6, 7</td></tr><tr><td>4</td><td>7</td></tr><tr><td>5</td><td>0, 8, 9</td></tr><tr><td>6</td><td>-</td></tr><tr><td>7</td><td>0, 2, 3</td></tr><tr><td>8</td><td>0, 3, 3, 3, 5</td></tr><tr><td>9</td><td>1, 3, 4, 9</td></tr></table> |

<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 127. Min: 73.

Mean: 97.74. Standard deviation: 9.55.

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