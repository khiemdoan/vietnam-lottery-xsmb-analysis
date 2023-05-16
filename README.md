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
| <table><tr><td>Date</td><td>16-05-2023</td></tr><tr><td>Special</td><td>19031</td></tr><tr><td>First</td><td>78859</td></tr><tr><td>Second</td><td>78392, 19184</td></tr><tr><td rowspan="2">Third</td><td>08741, 22539, 53479</td></tr><tr><td>89302, 45138, 93780</td></tr><tr><td>Fourth</td><td>6799, 1870, 9094, 5813</td></tr><tr><td rowspan="2">Fifth</td><td>5658, 5031, 1982</td></tr><tr><td>9514, 0651, 7630</td></tr><tr><td>Sixth</td><td>208, 378, 741</td></tr><tr><td>Seventh</td><td>63, 37, 82, 49</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 8</td></tr><tr><td>1</td><td>3, 4</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>0, 1, 1, 7, 8, 9</td></tr><tr><td>4</td><td>1, 1, 9</td></tr><tr><td>5</td><td>1, 8, 9</td></tr><tr><td>6</td><td>3</td></tr><tr><td>7</td><td>0, 8, 9</td></tr><tr><td>8</td><td>0, 2, 2, 4</td></tr><tr><td>9</td><td>2, 4, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 73.

Mean: 97.47. Standard deviation: 10.39.

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