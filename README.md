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
| <table><tr><td>Date</td><td>31-07-2023</td></tr><tr><td>Special</td><td>72615</td></tr><tr><td>First</td><td>73596</td></tr><tr><td>Second</td><td>29471, 16196</td></tr><tr><td rowspan="2">Third</td><td>13165, 43789, 59867</td></tr><tr><td>86590, 66461, 38341</td></tr><tr><td>Fourth</td><td>8590, 7894, 7401, 6477</td></tr><tr><td rowspan="2">Fifth</td><td>4560, 1221, 7202</td></tr><tr><td>7931, 7306, 9952</td></tr><tr><td>Sixth</td><td>802, 683, 737</td></tr><tr><td>Seventh</td><td>61, 76, 39, 36</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 2, 2, 6</td></tr><tr><td>1</td><td>5</td></tr><tr><td>2</td><td>1</td></tr><tr><td>3</td><td>1, 6, 7, 9</td></tr><tr><td>4</td><td>1</td></tr><tr><td>5</td><td>2</td></tr><tr><td>6</td><td>0, 1, 1, 5, 7</td></tr><tr><td>7</td><td>1, 6, 7</td></tr><tr><td>8</td><td>3, 9</td></tr><tr><td>9</td><td>0, 0, 4, 6, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 131. Min: 76.

Mean: 97.47. Standard deviation: 10.23.

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