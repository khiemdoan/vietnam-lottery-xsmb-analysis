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
| <table><tr><td>Date</td><td>05-03-2024</td></tr><tr><td>Special</td><td>87122</td></tr><tr><td>First</td><td>64388</td></tr><tr><td>Second</td><td>51684, 45089</td></tr><tr><td rowspan="2">Third</td><td>15702, 11869, 95889</td></tr><tr><td>95412, 35845, 75289</td></tr><tr><td>Fourth</td><td>3651, 7848, 0102, 9621</td></tr><tr><td rowspan="2">Fifth</td><td>1951, 8583, 0029</td></tr><tr><td>9692, 0278, 9912</td></tr><tr><td>Sixth</td><td>300, 105, 083</td></tr><tr><td>Seventh</td><td>75, 26, 18, 99</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 2, 2, 5</td></tr><tr><td>1</td><td>2, 2, 8</td></tr><tr><td>2</td><td>1, 2, 6, 9</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>5, 8</td></tr><tr><td>5</td><td>1, 1</td></tr><tr><td>6</td><td>9</td></tr><tr><td>7</td><td>5, 8</td></tr><tr><td>8</td><td>3, 3, 4, 8, 9, 9, 9</td></tr><tr><td>9</td><td>2, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 79.

Mean: 97.74. Standard deviation: 8.86.

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