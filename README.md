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
| <table><tr><td>Date</td><td>11-06-2023</td></tr><tr><td>Special</td><td>46260</td></tr><tr><td>First</td><td>22720</td></tr><tr><td>Second</td><td>81504, 02173</td></tr><tr><td rowspan="2">Third</td><td>16658, 20643, 72434</td></tr><tr><td>05068, 21857, 41825</td></tr><tr><td>Fourth</td><td>1921, 6654, 3727, 7848</td></tr><tr><td rowspan="2">Fifth</td><td>6263, 0249, 2221</td></tr><tr><td>9684, 5345, 4156</td></tr><tr><td>Sixth</td><td>967, 239, 243</td></tr><tr><td>Seventh</td><td>96, 57, 78, 64</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>4</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>0, 1, 1, 5, 7</td></tr><tr><td>3</td><td>4, 9</td></tr><tr><td>4</td><td>3, 3, 5, 8, 9</td></tr><tr><td>5</td><td>4, 6, 7, 7, 8</td></tr><tr><td>6</td><td>0, 3, 4, 7, 8</td></tr><tr><td>7</td><td>3, 8</td></tr><tr><td>8</td><td>4</td></tr><tr><td>9</td><td>6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 124. Min: 76.

Mean: 97.47. Standard deviation: 10.35.

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