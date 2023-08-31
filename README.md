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
| <table><tr><td>Date</td><td>31-08-2023</td></tr><tr><td>Special</td><td>73040</td></tr><tr><td>First</td><td>49951</td></tr><tr><td>Second</td><td>45966, 86381</td></tr><tr><td rowspan="2">Third</td><td>41593, 00092, 86954</td></tr><tr><td>84340, 47439, 63862</td></tr><tr><td>Fourth</td><td>2848, 7645, 3439, 0211</td></tr><tr><td rowspan="2">Fifth</td><td>1304, 4480, 3555</td></tr><tr><td>3946, 5126, 3834</td></tr><tr><td>Sixth</td><td>166, 251, 788</td></tr><tr><td>Seventh</td><td>52, 05, 29, 62</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>4, 5</td></tr><tr><td>1</td><td>1</td></tr><tr><td>2</td><td>6, 9</td></tr><tr><td>3</td><td>4, 9, 9</td></tr><tr><td>4</td><td>0, 0, 5, 6, 8</td></tr><tr><td>5</td><td>1, 1, 2, 4, 5</td></tr><tr><td>6</td><td>2, 2, 6, 6</td></tr><tr><td>7</td><td>-</td></tr><tr><td>8</td><td>0, 1, 8</td></tr><tr><td>9</td><td>2, 3</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 122. Min: 78.

Mean: 97.47. Standard deviation: 10.26.

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