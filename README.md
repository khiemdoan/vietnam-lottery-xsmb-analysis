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
| <table><tr><td>Date</td><td>26-03-2023</td></tr><tr><td>Special</td><td>57765</td></tr><tr><td>First</td><td>81664</td></tr><tr><td>Second</td><td>81817, 24222</td></tr><tr><td rowspan="2">Third</td><td>29370, 84409, 04923</td></tr><tr><td>57889, 07071, 93934</td></tr><tr><td>Fourth</td><td>4102, 2973, 6263, 6666</td></tr><tr><td rowspan="2">Fifth</td><td>8566, 3378, 2688</td></tr><tr><td>1310, 3160, 6446</td></tr><tr><td>Sixth</td><td>895, 560, 344</td></tr><tr><td>Seventh</td><td>30, 52, 63, 13</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 9</td></tr><tr><td>1</td><td>0, 3, 7</td></tr><tr><td>2</td><td>2, 3</td></tr><tr><td>3</td><td>0, 4</td></tr><tr><td>4</td><td>4, 6</td></tr><tr><td>5</td><td>2</td></tr><tr><td>6</td><td>0, 0, 3, 3, 4, 5, 6, 6</td></tr><tr><td>7</td><td>0, 1, 3, 8</td></tr><tr><td>8</td><td>8, 9</td></tr><tr><td>9</td><td>5</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 73.

Mean: 97.47. Standard deviation: 11.16.

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