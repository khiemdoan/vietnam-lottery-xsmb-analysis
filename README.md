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
| <table><tr><td>Date</td><td>06-04-2023</td></tr><tr><td>Special</td><td>89911</td></tr><tr><td>First</td><td>05742</td></tr><tr><td>Second</td><td>50512, 78149</td></tr><tr><td rowspan="2">Third</td><td>88171, 00910, 17405</td></tr><tr><td>26389, 88291, 99363</td></tr><tr><td>Fourth</td><td>7605, 2631, 8658, 7044</td></tr><tr><td rowspan="2">Fifth</td><td>8351, 4521, 5193</td></tr><tr><td>7433, 2793, 6406</td></tr><tr><td>Sixth</td><td>436, 412, 634</td></tr><tr><td>Seventh</td><td>60, 25, 68, 65</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>5, 5, 6</td></tr><tr><td>1</td><td>0, 1, 2, 2</td></tr><tr><td>2</td><td>1, 5</td></tr><tr><td>3</td><td>1, 3, 4, 6</td></tr><tr><td>4</td><td>2, 4, 9</td></tr><tr><td>5</td><td>1, 8</td></tr><tr><td>6</td><td>0, 3, 5, 8</td></tr><tr><td>7</td><td>1</td></tr><tr><td>8</td><td>9</td></tr><tr><td>9</td><td>1, 3, 3</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 121. Min: 74.

Mean: 97.47. Standard deviation: 11.21.

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