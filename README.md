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
| <table><tr><td>Date</td><td>25-06-2023</td></tr><tr><td>Special</td><td>63634</td></tr><tr><td>First</td><td>89812</td></tr><tr><td>Second</td><td>83546, 02844</td></tr><tr><td rowspan="2">Third</td><td>03095, 31835, 01834</td></tr><tr><td>53707, 10733, 27255</td></tr><tr><td>Fourth</td><td>2684, 8989, 2268, 5181</td></tr><tr><td rowspan="2">Fifth</td><td>0406, 8073, 3678</td></tr><tr><td>8809, 0787, 7548</td></tr><tr><td>Sixth</td><td>446, 547, 268</td></tr><tr><td>Seventh</td><td>43, 62, 13, 16</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>6, 7, 9</td></tr><tr><td>1</td><td>2, 3, 6</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>3, 4, 4, 5</td></tr><tr><td>4</td><td>3, 4, 6, 6, 7, 8</td></tr><tr><td>5</td><td>5</td></tr><tr><td>6</td><td>2, 8, 8</td></tr><tr><td>7</td><td>3, 8</td></tr><tr><td>8</td><td>1, 4, 7, 9</td></tr><tr><td>9</td><td>5</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 76.

Mean: 97.47. Standard deviation: 10.11.

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