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
| <table><tr><td>Date</td><td>08-03-2024</td></tr><tr><td>Special</td><td>71307</td></tr><tr><td>First</td><td>20243</td></tr><tr><td>Second</td><td>17094, 60989</td></tr><tr><td rowspan="2">Third</td><td>31527, 92382, 96787</td></tr><tr><td>36794, 48482, 77297</td></tr><tr><td>Fourth</td><td>5626, 6650, 0211, 7778</td></tr><tr><td rowspan="2">Fifth</td><td>1022, 8863, 9869</td></tr><tr><td>7124, 5225, 1665</td></tr><tr><td>Sixth</td><td>011, 087, 756</td></tr><tr><td>Seventh</td><td>52, 14, 44, 43</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>7</td></tr><tr><td>1</td><td>1, 1, 4</td></tr><tr><td>2</td><td>2, 4, 5, 6, 7</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>3, 3, 4</td></tr><tr><td>5</td><td>0, 2, 6</td></tr><tr><td>6</td><td>3, 5, 9</td></tr><tr><td>7</td><td>8</td></tr><tr><td>8</td><td>2, 2, 7, 7, 9</td></tr><tr><td>9</td><td>4, 4, 7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 119. Min: 79.

Mean: 97.74. Standard deviation: 8.81.

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