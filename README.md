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
| <table><tr><td>Date</td><td>20-02-2024</td></tr><tr><td>Special</td><td>57406</td></tr><tr><td>First</td><td>97758</td></tr><tr><td>Second</td><td>37216, 24939</td></tr><tr><td rowspan="2">Third</td><td>30032, 78750, 31430</td></tr><tr><td>43822, 43341, 22605</td></tr><tr><td>Fourth</td><td>7939, 8580, 7131, 0783</td></tr><tr><td rowspan="2">Fifth</td><td>0866, 9656, 7260</td></tr><tr><td>4515, 7573, 3621</td></tr><tr><td>Sixth</td><td>592, 419, 079</td></tr><tr><td>Seventh</td><td>68, 18, 78, 00</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 5, 6</td></tr><tr><td>1</td><td>5, 6, 8, 9</td></tr><tr><td>2</td><td>1, 2</td></tr><tr><td>3</td><td>0, 1, 2, 9, 9</td></tr><tr><td>4</td><td>1</td></tr><tr><td>5</td><td>0, 6, 8</td></tr><tr><td>6</td><td>0, 6, 8</td></tr><tr><td>7</td><td>3, 8, 9</td></tr><tr><td>8</td><td>0, 3</td></tr><tr><td>9</td><td>2</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 79.

Mean: 97.47. Standard deviation: 8.78.

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