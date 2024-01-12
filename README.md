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
| <table><tr><td>Date</td><td>12-01-2024</td></tr><tr><td>Special</td><td>13113</td></tr><tr><td>First</td><td>39786</td></tr><tr><td>Second</td><td>66200, 15781</td></tr><tr><td rowspan="2">Third</td><td>57716, 05600, 89058</td></tr><tr><td>37477, 31125, 85815</td></tr><tr><td>Fourth</td><td>2872, 4210, 3055, 7656</td></tr><tr><td rowspan="2">Fifth</td><td>5975, 9865, 4483</td></tr><tr><td>4984, 9833, 9996</td></tr><tr><td>Sixth</td><td>906, 600, 547</td></tr><tr><td>Seventh</td><td>02, 93, 53, 59</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 0, 0, 2, 6</td></tr><tr><td>1</td><td>0, 3, 5, 6</td></tr><tr><td>2</td><td>5</td></tr><tr><td>3</td><td>3</td></tr><tr><td>4</td><td>7</td></tr><tr><td>5</td><td>3, 5, 6, 8, 9</td></tr><tr><td>6</td><td>5</td></tr><tr><td>7</td><td>2, 5, 7</td></tr><tr><td>8</td><td>1, 3, 4, 6</td></tr><tr><td>9</td><td>3, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 77.

Mean: 97.47. Standard deviation: 9.16.

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