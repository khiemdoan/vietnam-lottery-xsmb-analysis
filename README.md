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
| <table><tr><td>Date</td><td>07-03-2024</td></tr><tr><td>Special</td><td>03047</td></tr><tr><td>First</td><td>58941</td></tr><tr><td>Second</td><td>47442, 56737</td></tr><tr><td rowspan="2">Third</td><td>55967, 75948, 24885</td></tr><tr><td>07736, 02093, 56900</td></tr><tr><td>Fourth</td><td>7490, 0152, 5300, 7005</td></tr><tr><td rowspan="2">Fifth</td><td>8175, 5037, 6867</td></tr><tr><td>7425, 8500, 7138</td></tr><tr><td>Sixth</td><td>385, 939, 306</td></tr><tr><td>Seventh</td><td>33, 86, 49, 82</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 0, 0, 5, 6</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>5</td></tr><tr><td>3</td><td>3, 6, 7, 7, 8, 9</td></tr><tr><td>4</td><td>1, 2, 7, 8, 9</td></tr><tr><td>5</td><td>2</td></tr><tr><td>6</td><td>7, 7</td></tr><tr><td>7</td><td>5</td></tr><tr><td>8</td><td>2, 5, 5, 6</td></tr><tr><td>9</td><td>0, 3</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 79.

Mean: 97.74. Standard deviation: 8.83.

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