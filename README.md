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
| <table><tr><td>Date</td><td>13-12-2023</td></tr><tr><td>Special</td><td>91706</td></tr><tr><td>First</td><td>82736</td></tr><tr><td>Second</td><td>43914, 21410</td></tr><tr><td rowspan="2">Third</td><td>62100, 28841, 54653</td></tr><tr><td>02003, 00059, 46346</td></tr><tr><td>Fourth</td><td>3044, 7942, 3115, 2346</td></tr><tr><td rowspan="2">Fifth</td><td>2092, 6475, 3946</td></tr><tr><td>3685, 3452, 1207</td></tr><tr><td>Sixth</td><td>346, 956, 814</td></tr><tr><td>Seventh</td><td>55, 83, 76, 44</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 3, 6, 7</td></tr><tr><td>1</td><td>0, 4, 4, 5</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>6</td></tr><tr><td>4</td><td>1, 2, 4, 4, 6, 6, 6, 6</td></tr><tr><td>5</td><td>2, 3, 5, 6, 9</td></tr><tr><td>6</td><td>-</td></tr><tr><td>7</td><td>5, 6</td></tr><tr><td>8</td><td>3, 5</td></tr><tr><td>9</td><td>2</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 129. Min: 77.

Mean: 97.47. Standard deviation: 9.42.

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