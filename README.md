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
| <table><tr><td>Date</td><td>10-05-2023</td></tr><tr><td>Special</td><td>97996</td></tr><tr><td>First</td><td>66184</td></tr><tr><td>Second</td><td>81579, 19025</td></tr><tr><td rowspan="2">Third</td><td>25267, 82002, 34364</td></tr><tr><td>80746, 09850, 02979</td></tr><tr><td>Fourth</td><td>5509, 2451, 3535, 0484</td></tr><tr><td rowspan="2">Fifth</td><td>9156, 1859, 0249</td></tr><tr><td>6927, 7902, 2659</td></tr><tr><td>Sixth</td><td>556, 891, 491</td></tr><tr><td>Seventh</td><td>05, 43, 19, 84</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 2, 5, 9</td></tr><tr><td>1</td><td>9</td></tr><tr><td>2</td><td>5, 7</td></tr><tr><td>3</td><td>5</td></tr><tr><td>4</td><td>3, 6, 9</td></tr><tr><td>5</td><td>0, 1, 6, 6, 9, 9</td></tr><tr><td>6</td><td>4, 7</td></tr><tr><td>7</td><td>9, 9</td></tr><tr><td>8</td><td>4, 4, 4</td></tr><tr><td>9</td><td>1, 1, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 120. Min: 73.

Mean: 97.47. Standard deviation: 10.47.

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