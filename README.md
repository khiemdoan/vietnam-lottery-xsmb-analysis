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
| <table><tr><td>Date</td><td>21-12-2023</td></tr><tr><td>Special</td><td>88485</td></tr><tr><td>First</td><td>81423</td></tr><tr><td>Second</td><td>48393, 07890</td></tr><tr><td rowspan="2">Third</td><td>51946, 07983, 63690</td></tr><tr><td>09200, 68261, 08586</td></tr><tr><td>Fourth</td><td>8909, 1980, 4697, 9087</td></tr><tr><td rowspan="2">Fifth</td><td>9687, 9617, 6090</td></tr><tr><td>8526, 3279, 9866</td></tr><tr><td>Sixth</td><td>403, 775, 949</td></tr><tr><td>Seventh</td><td>83, 21, 41, 81</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 3, 9</td></tr><tr><td>1</td><td>7</td></tr><tr><td>2</td><td>1, 3, 6</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>1, 6, 9</td></tr><tr><td>5</td><td>-</td></tr><tr><td>6</td><td>1, 6</td></tr><tr><td>7</td><td>5, 9</td></tr><tr><td>8</td><td>0, 1, 3, 3, 5, 6, 7, 7</td></tr><tr><td>9</td><td>0, 0, 0, 3, 7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 131. Min: 79.

Mean: 97.47. Standard deviation: 9.29.

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