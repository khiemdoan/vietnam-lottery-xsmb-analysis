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
| <table><tr><td>Date</td><td>23-02-2024</td></tr><tr><td>Special</td><td>16053</td></tr><tr><td>First</td><td>88635</td></tr><tr><td>Second</td><td>25337, 63488</td></tr><tr><td rowspan="2">Third</td><td>59775, 29439, 27290</td></tr><tr><td>24040, 82530, 67189</td></tr><tr><td>Fourth</td><td>0547, 6741, 7941, 7289</td></tr><tr><td rowspan="2">Fifth</td><td>7824, 5469, 8625</td></tr><tr><td>7168, 1204, 5983</td></tr><tr><td>Sixth</td><td>308, 973, 820</td></tr><tr><td>Seventh</td><td>79, 00, 93, 45</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 4, 8</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>0, 4, 5</td></tr><tr><td>3</td><td>0, 5, 7, 9</td></tr><tr><td>4</td><td>0, 1, 1, 5, 7</td></tr><tr><td>5</td><td>3</td></tr><tr><td>6</td><td>8, 9</td></tr><tr><td>7</td><td>3, 5, 9</td></tr><tr><td>8</td><td>3, 8, 9, 9</td></tr><tr><td>9</td><td>0, 3</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 119. Min: 79.

Mean: 97.47. Standard deviation: 8.57.

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