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
| <table><tr><td>Date</td><td>21-09-2023</td></tr><tr><td>Special</td><td>52566</td></tr><tr><td>First</td><td>34841</td></tr><tr><td>Second</td><td>51527, 93225</td></tr><tr><td rowspan="2">Third</td><td>11728, 25151, 80780</td></tr><tr><td>49217, 55120, 57854</td></tr><tr><td>Fourth</td><td>0466, 4980, 0563, 6846</td></tr><tr><td rowspan="2">Fifth</td><td>6189, 5380, 9292</td></tr><tr><td>6703, 4758, 9247</td></tr><tr><td>Sixth</td><td>104, 794, 694</td></tr><tr><td>Seventh</td><td>64, 63, 21, 91</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>3, 4</td></tr><tr><td>1</td><td>7</td></tr><tr><td>2</td><td>0, 1, 5, 7, 8</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>1, 6, 7</td></tr><tr><td>5</td><td>1, 4, 8</td></tr><tr><td>6</td><td>3, 3, 4, 6, 6</td></tr><tr><td>7</td><td>-</td></tr><tr><td>8</td><td>0, 0, 0, 9</td></tr><tr><td>9</td><td>1, 2, 4, 4</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 124. Min: 77.

Mean: 97.47. Standard deviation: 9.9.

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