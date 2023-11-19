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
| <table><tr><td>Date</td><td>19-11-2023</td></tr><tr><td>Special</td><td>38429</td></tr><tr><td>First</td><td>02633</td></tr><tr><td>Second</td><td>37498, 40297</td></tr><tr><td rowspan="2">Third</td><td>14331, 95638, 82894</td></tr><tr><td>72723, 51994, 85732</td></tr><tr><td>Fourth</td><td>1243, 0254, 8383, 9997</td></tr><tr><td rowspan="2">Fifth</td><td>2136, 7389, 6623</td></tr><tr><td>6224, 6833, 9192</td></tr><tr><td>Sixth</td><td>062, 766, 980</td></tr><tr><td>Seventh</td><td>28, 19, 90, 64</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>9</td></tr><tr><td>2</td><td>3, 3, 4, 8, 9</td></tr><tr><td>3</td><td>1, 2, 3, 3, 6, 8</td></tr><tr><td>4</td><td>3</td></tr><tr><td>5</td><td>4</td></tr><tr><td>6</td><td>2, 4, 6</td></tr><tr><td>7</td><td>-</td></tr><tr><td>8</td><td>0, 3, 9</td></tr><tr><td>9</td><td>0, 2, 4, 4, 7, 7, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 128. Min: 77.

Mean: 97.47. Standard deviation: 9.61.

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