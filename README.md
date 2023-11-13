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
| <table><tr><td>Date</td><td>13-11-2023</td></tr><tr><td>Special</td><td>19412</td></tr><tr><td>First</td><td>85667</td></tr><tr><td>Second</td><td>26906, 22710</td></tr><tr><td rowspan="2">Third</td><td>09590, 96248, 53294</td></tr><tr><td>43395, 49876, 53705</td></tr><tr><td>Fourth</td><td>0546, 8664, 1572, 8719</td></tr><tr><td rowspan="2">Fifth</td><td>5678, 1599, 1893</td></tr><tr><td>6844, 0749, 9130</td></tr><tr><td>Sixth</td><td>503, 719, 868</td></tr><tr><td>Seventh</td><td>31, 11, 43, 35</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>3, 5, 6</td></tr><tr><td>1</td><td>0, 1, 2, 9, 9</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>0, 1, 5</td></tr><tr><td>4</td><td>3, 4, 6, 8, 9</td></tr><tr><td>5</td><td>-</td></tr><tr><td>6</td><td>4, 7, 8</td></tr><tr><td>7</td><td>2, 6, 8</td></tr><tr><td>8</td><td>-</td></tr><tr><td>9</td><td>0, 3, 4, 5, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 77.

Mean: 97.47. Standard deviation: 9.26.

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