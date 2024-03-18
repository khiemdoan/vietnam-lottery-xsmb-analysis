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
| <table><tr><td>Date</td><td>18-03-2024</td></tr><tr><td>Special</td><td>78723</td></tr><tr><td>First</td><td>05913</td></tr><tr><td>Second</td><td>42978, 47997</td></tr><tr><td rowspan="2">Third</td><td>12779, 25923, 66649</td></tr><tr><td>28808, 79008, 51224</td></tr><tr><td>Fourth</td><td>4813, 1627, 6276, 4906</td></tr><tr><td rowspan="2">Fifth</td><td>6495, 7729, 2690</td></tr><tr><td>7389, 9423, 1047</td></tr><tr><td>Sixth</td><td>902, 463, 762</td></tr><tr><td>Seventh</td><td>82, 29, 25, 53</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 6, 8, 8</td></tr><tr><td>1</td><td>3, 3</td></tr><tr><td>2</td><td>3, 3, 3, 4, 5, 7, 9, 9</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>7, 9</td></tr><tr><td>5</td><td>3</td></tr><tr><td>6</td><td>2, 3</td></tr><tr><td>7</td><td>6, 8, 9</td></tr><tr><td>8</td><td>2, 9</td></tr><tr><td>9</td><td>0, 5, 7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 121. Min: 79.

Mean: 97.74. Standard deviation: 8.79.

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