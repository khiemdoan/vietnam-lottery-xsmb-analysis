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
| <table><tr><td>Date</td><td>18-03-2023</td></tr><tr><td>Special</td><td>57570</td></tr><tr><td>First</td><td>25444</td></tr><tr><td>Second</td><td>05260, 51308</td></tr><tr><td rowspan="2">Third</td><td>14099, 69326, 17323</td></tr><tr><td>52596, 06495, 47274</td></tr><tr><td>Fourth</td><td>1522, 2679, 3931, 2502</td></tr><tr><td rowspan="2">Fifth</td><td>2734, 6503, 6147</td></tr><tr><td>0437, 5088, 0227</td></tr><tr><td>Sixth</td><td>897, 979, 581</td></tr><tr><td>Seventh</td><td>44, 97, 13, 93</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 3, 8</td></tr><tr><td>1</td><td>3</td></tr><tr><td>2</td><td>2, 3, 6, 7</td></tr><tr><td>3</td><td>1, 4, 7</td></tr><tr><td>4</td><td>4, 4, 7</td></tr><tr><td>5</td><td>-</td></tr><tr><td>6</td><td>0</td></tr><tr><td>7</td><td>0, 4, 9, 9</td></tr><tr><td>8</td><td>1, 8</td></tr><tr><td>9</td><td>3, 5, 6, 7, 7, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 75.

Mean: 97.47. Standard deviation: 11.24.

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