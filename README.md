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
| <table><tr><td>Date</td><td>01-08-2023</td></tr><tr><td>Special</td><td>04430</td></tr><tr><td>First</td><td>18971</td></tr><tr><td>Second</td><td>47120, 00337</td></tr><tr><td rowspan="2">Third</td><td>11167, 95150, 31425</td></tr><tr><td>22107, 44661, 79135</td></tr><tr><td>Fourth</td><td>9009, 8851, 5221, 3489</td></tr><tr><td rowspan="2">Fifth</td><td>6446, 9609, 5128</td></tr><tr><td>7304, 3140, 7896</td></tr><tr><td>Sixth</td><td>731, 874, 836</td></tr><tr><td>Seventh</td><td>90, 95, 72, 85</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>4, 7, 9, 9</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>0, 1, 5, 8</td></tr><tr><td>3</td><td>0, 1, 5, 6, 7</td></tr><tr><td>4</td><td>0, 6</td></tr><tr><td>5</td><td>0, 1</td></tr><tr><td>6</td><td>1, 7</td></tr><tr><td>7</td><td>1, 2, 4</td></tr><tr><td>8</td><td>5, 9</td></tr><tr><td>9</td><td>0, 5, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 131. Min: 76.

Mean: 97.47. Standard deviation: 10.26.

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