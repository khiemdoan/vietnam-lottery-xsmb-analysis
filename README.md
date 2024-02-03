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
| <table><tr><td>Date</td><td>03-02-2024</td></tr><tr><td>Special</td><td>33389</td></tr><tr><td>First</td><td>80369</td></tr><tr><td>Second</td><td>55380, 69435</td></tr><tr><td rowspan="2">Third</td><td>92942, 94293, 36365</td></tr><tr><td>34162, 09641, 10284</td></tr><tr><td>Fourth</td><td>0221, 1633, 1716, 6658</td></tr><tr><td rowspan="2">Fifth</td><td>0122, 2297, 2514</td></tr><tr><td>8365, 7192, 3441</td></tr><tr><td>Sixth</td><td>236, 119, 442</td></tr><tr><td>Seventh</td><td>12, 35, 88, 18</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>2, 4, 6, 8, 9</td></tr><tr><td>2</td><td>1, 2</td></tr><tr><td>3</td><td>3, 5, 5, 6</td></tr><tr><td>4</td><td>1, 1, 2, 2</td></tr><tr><td>5</td><td>8</td></tr><tr><td>6</td><td>2, 5, 5, 9</td></tr><tr><td>7</td><td>-</td></tr><tr><td>8</td><td>0, 4, 8, 9</td></tr><tr><td>9</td><td>2, 3, 7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 81.

Mean: 98.55. Standard deviation: 8.99.

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