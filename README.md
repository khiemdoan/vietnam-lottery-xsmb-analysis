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
| <table><tr><td>Date</td><td>12-06-2023</td></tr><tr><td>Special</td><td>55442</td></tr><tr><td>First</td><td>33251</td></tr><tr><td>Second</td><td>65623, 42048</td></tr><tr><td rowspan="2">Third</td><td>68726, 89403, 20511</td></tr><tr><td>62202, 52994, 94397</td></tr><tr><td>Fourth</td><td>1802, 7934, 2963, 1958</td></tr><tr><td rowspan="2">Fifth</td><td>7198, 5514, 8294</td></tr><tr><td>7181, 1766, 9753</td></tr><tr><td>Sixth</td><td>273, 439, 837</td></tr><tr><td>Seventh</td><td>01, 39, 63, 68</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 2, 2, 3</td></tr><tr><td>1</td><td>1, 4</td></tr><tr><td>2</td><td>3, 6</td></tr><tr><td>3</td><td>4, 7, 9, 9</td></tr><tr><td>4</td><td>2, 8</td></tr><tr><td>5</td><td>1, 3, 8</td></tr><tr><td>6</td><td>3, 3, 6, 8</td></tr><tr><td>7</td><td>3</td></tr><tr><td>8</td><td>1</td></tr><tr><td>9</td><td>4, 4, 7, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 78.

Mean: 97.47. Standard deviation: 10.22.

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