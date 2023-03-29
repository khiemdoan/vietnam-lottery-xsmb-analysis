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
| <table><tr><td>Date</td><td>29-03-2023</td></tr><tr><td>Special</td><td>86367</td></tr><tr><td>First</td><td>69313</td></tr><tr><td>Second</td><td>57644, 99117</td></tr><tr><td rowspan="2">Third</td><td>57068, 01410, 71666</td></tr><tr><td>59756, 37373, 20474</td></tr><tr><td>Fourth</td><td>6395, 5291, 5632, 3556</td></tr><tr><td rowspan="2">Fifth</td><td>2533, 5880, 4616</td></tr><tr><td>8998, 7741, 1916</td></tr><tr><td>Sixth</td><td>961, 316, 203</td></tr><tr><td>Seventh</td><td>60, 85, 39, 71</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>3</td></tr><tr><td>1</td><td>0, 3, 6, 6, 6, 7</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>2, 3, 9</td></tr><tr><td>4</td><td>1, 4</td></tr><tr><td>5</td><td>6, 6</td></tr><tr><td>6</td><td>0, 1, 6, 7, 8</td></tr><tr><td>7</td><td>1, 3, 4</td></tr><tr><td>8</td><td>0, 5</td></tr><tr><td>9</td><td>1, 5, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 72.

Mean: 97.47. Standard deviation: 11.41.

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