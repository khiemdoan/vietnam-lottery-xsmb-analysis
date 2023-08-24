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
| <table><tr><td>Date</td><td>24-08-2023</td></tr><tr><td>Special</td><td>57973</td></tr><tr><td>First</td><td>56968</td></tr><tr><td>Second</td><td>14617, 65709</td></tr><tr><td rowspan="2">Third</td><td>80552, 37370, 15250</td></tr><tr><td>20440, 22904, 77493</td></tr><tr><td>Fourth</td><td>7257, 1247, 1466, 9018</td></tr><tr><td rowspan="2">Fifth</td><td>2216, 9070, 9700</td></tr><tr><td>0651, 3860, 3967</td></tr><tr><td>Sixth</td><td>696, 165, 515</td></tr><tr><td>Seventh</td><td>58, 49, 66, 44</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 4, 9</td></tr><tr><td>1</td><td>5, 6, 7, 8</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>0, 4, 7, 9</td></tr><tr><td>5</td><td>0, 1, 2, 7, 8</td></tr><tr><td>6</td><td>0, 5, 6, 6, 7, 8</td></tr><tr><td>7</td><td>0, 0, 3</td></tr><tr><td>8</td><td>-</td></tr><tr><td>9</td><td>3, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 76.

Mean: 97.47. Standard deviation: 10.28.

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