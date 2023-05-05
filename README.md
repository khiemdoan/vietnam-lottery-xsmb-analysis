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
| <table><tr><td>Date</td><td>05-05-2023</td></tr><tr><td>Special</td><td>82647</td></tr><tr><td>First</td><td>95546</td></tr><tr><td>Second</td><td>39378, 98658</td></tr><tr><td rowspan="2">Third</td><td>97994, 13760, 07192</td></tr><tr><td>61645, 91254, 34455</td></tr><tr><td>Fourth</td><td>5511, 4527, 0642, 4236</td></tr><tr><td rowspan="2">Fifth</td><td>0155, 7861, 2259</td></tr><tr><td>0242, 1787, 5726</td></tr><tr><td>Sixth</td><td>432, 624, 534</td></tr><tr><td>Seventh</td><td>16, 14, 72, 39</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>1, 4, 6</td></tr><tr><td>2</td><td>4, 6, 7</td></tr><tr><td>3</td><td>2, 4, 6, 9</td></tr><tr><td>4</td><td>2, 2, 5, 6, 7</td></tr><tr><td>5</td><td>4, 5, 5, 8, 9</td></tr><tr><td>6</td><td>0, 1</td></tr><tr><td>7</td><td>2, 8</td></tr><tr><td>8</td><td>7</td></tr><tr><td>9</td><td>2, 4</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 119. Min: 74.

Mean: 97.47. Standard deviation: 10.5.

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