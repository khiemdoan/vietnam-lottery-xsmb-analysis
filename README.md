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
| <table><tr><td>Date</td><td>14-11-2023</td></tr><tr><td>Special</td><td>85800</td></tr><tr><td>First</td><td>00197</td></tr><tr><td>Second</td><td>42692, 64848</td></tr><tr><td rowspan="2">Third</td><td>29100, 63052, 36810</td></tr><tr><td>40639, 42349, 75155</td></tr><tr><td>Fourth</td><td>3675, 2498, 3669, 6507</td></tr><tr><td rowspan="2">Fifth</td><td>9587, 3898, 3298</td></tr><tr><td>5302, 4643, 3914</td></tr><tr><td>Sixth</td><td>066, 614, 953</td></tr><tr><td>Seventh</td><td>36, 97, 41, 57</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 0, 2, 7</td></tr><tr><td>1</td><td>0, 4, 4</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>6, 9</td></tr><tr><td>4</td><td>1, 3, 8, 9</td></tr><tr><td>5</td><td>2, 3, 5, 7</td></tr><tr><td>6</td><td>6, 9</td></tr><tr><td>7</td><td>5</td></tr><tr><td>8</td><td>7</td></tr><tr><td>9</td><td>2, 7, 7, 8, 8, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 77.

Mean: 97.47. Standard deviation: 9.23.

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