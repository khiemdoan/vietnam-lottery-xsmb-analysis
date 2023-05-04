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
| <table><tr><td>Date</td><td>04-05-2023</td></tr><tr><td>Special</td><td>81918</td></tr><tr><td>First</td><td>25824</td></tr><tr><td>Second</td><td>12136, 10697</td></tr><tr><td rowspan="2">Third</td><td>61949, 33310, 79061</td></tr><tr><td>22400, 85742, 85067</td></tr><tr><td>Fourth</td><td>1177, 4922, 6028, 9883</td></tr><tr><td rowspan="2">Fifth</td><td>4177, 1011, 8968</td></tr><tr><td>3260, 7500, 7006</td></tr><tr><td>Sixth</td><td>561, 096, 553</td></tr><tr><td>Seventh</td><td>87, 35, 49, 42</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 0, 6</td></tr><tr><td>1</td><td>0, 1, 8</td></tr><tr><td>2</td><td>2, 4, 8</td></tr><tr><td>3</td><td>5, 6</td></tr><tr><td>4</td><td>2, 2, 9, 9</td></tr><tr><td>5</td><td>3</td></tr><tr><td>6</td><td>0, 1, 1, 7, 8</td></tr><tr><td>7</td><td>7, 7</td></tr><tr><td>8</td><td>3, 7</td></tr><tr><td>9</td><td>6, 7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 118. Min: 75.

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