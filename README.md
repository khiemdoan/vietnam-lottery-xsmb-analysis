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
| <table><tr><td>Date (Ngày)</td><td>11-04-2024</td></tr><tr><td>Special (Giải dặc biệt)</td><td>69356</td></tr><tr><td>First (Giải nhất)</td><td>22552</td></tr><tr><td>Second (Giải nhì)</td><td>35140, 15293</td></tr><tr><td rowspan="2">Third (Giải ba)</td><td>35010, 28133, 33342</td></tr><tr><td>65578, 74436, 57981</td></tr><tr><td>Fourth (Giải tư)</td><td>4851, 2761, 8993, 3587</td></tr><tr><td rowspan="2">Fifth (Giải năm)</td><td>6909, 2693, 2363</td></tr><tr><td>1750, 3328, 7628</td></tr><tr><td>Sixth (Giải sáu)</td><td>753, 388, 635</td></tr><tr><td>Seventh (Giải bảy)</td><td>73, 80, 42, 86</td></tr></table> | <table><tr><td>First (Đầu)</td><td>Last (Đuôi)</td></tr><tr><td>0</td><td>9</td></tr><tr><td>1</td><td>0</td></tr><tr><td>2</td><td>8, 8</td></tr><tr><td>3</td><td>3, 5, 6</td></tr><tr><td>4</td><td>0, 2, 2</td></tr><tr><td>5</td><td>0, 1, 2, 3, 6</td></tr><tr><td>6</td><td>1, 3</td></tr><tr><td>7</td><td>3, 8</td></tr><tr><td>8</td><td>0, 1, 6, 7, 8</td></tr><tr><td>9</td><td>3, 3, 3</td></tr></table> |

<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 127. Min: 72.

Mean: 97.74. Standard deviation: 9.54.

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