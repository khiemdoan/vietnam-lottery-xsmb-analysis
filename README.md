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
| <table><tr><td>Date</td><td>08-12-2023</td></tr><tr><td>Special</td><td>38223</td></tr><tr><td>First</td><td>77286</td></tr><tr><td>Second</td><td>90185, 84473</td></tr><tr><td rowspan="2">Third</td><td>08584, 79697, 95286</td></tr><tr><td>76506, 43075, 76662</td></tr><tr><td>Fourth</td><td>7394, 0605, 4471, 5963</td></tr><tr><td rowspan="2">Fifth</td><td>1127, 8186, 4005</td></tr><tr><td>2106, 8507, 6915</td></tr><tr><td>Sixth</td><td>706, 481, 999</td></tr><tr><td>Seventh</td><td>06, 39, 93, 97</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>5, 5, 6, 6, 6, 6, 7</td></tr><tr><td>1</td><td>5</td></tr><tr><td>2</td><td>3, 7</td></tr><tr><td>3</td><td>9</td></tr><tr><td>4</td><td>-</td></tr><tr><td>5</td><td>-</td></tr><tr><td>6</td><td>2, 3</td></tr><tr><td>7</td><td>1, 3, 5</td></tr><tr><td>8</td><td>1, 4, 5, 6, 6, 6</td></tr><tr><td>9</td><td>3, 4, 7, 7, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 128. Min: 76.

Mean: 97.47. Standard deviation: 9.5.

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