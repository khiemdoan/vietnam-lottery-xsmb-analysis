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
| <table><tr><td>Date</td><td>26-01-2024</td></tr><tr><td>Special</td><td>20347</td></tr><tr><td>First</td><td>29197</td></tr><tr><td>Second</td><td>19218, 63399</td></tr><tr><td rowspan="2">Third</td><td>82560, 80548, 17544</td></tr><tr><td>73396, 45107, 10888</td></tr><tr><td>Fourth</td><td>4359, 6568, 4811, 1038</td></tr><tr><td rowspan="2">Fifth</td><td>1823, 8447, 2579</td></tr><tr><td>2491, 2352, 8442</td></tr><tr><td>Sixth</td><td>947, 733, 318</td></tr><tr><td>Seventh</td><td>58, 56, 20, 06</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>6, 7</td></tr><tr><td>1</td><td>1, 8, 8</td></tr><tr><td>2</td><td>0, 3</td></tr><tr><td>3</td><td>3, 8</td></tr><tr><td>4</td><td>2, 4, 7, 7, 7, 8</td></tr><tr><td>5</td><td>2, 6, 8, 9</td></tr><tr><td>6</td><td>0, 8</td></tr><tr><td>7</td><td>9</td></tr><tr><td>8</td><td>8</td></tr><tr><td>9</td><td>1, 6, 7, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 80.

Mean: 98.55. Standard deviation: 8.93.

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