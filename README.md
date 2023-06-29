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
| <table><tr><td>Date</td><td>29-06-2023</td></tr><tr><td>Special</td><td>06920</td></tr><tr><td>First</td><td>56675</td></tr><tr><td>Second</td><td>67716, 70226</td></tr><tr><td rowspan="2">Third</td><td>25883, 78117, 84401</td></tr><tr><td>10799, 94060, 69390</td></tr><tr><td>Fourth</td><td>0144, 9883, 7643, 6236</td></tr><tr><td rowspan="2">Fifth</td><td>3976, 0038, 5573</td></tr><tr><td>0135, 0392, 6592</td></tr><tr><td>Sixth</td><td>424, 847, 468</td></tr><tr><td>Seventh</td><td>13, 87, 98, 36</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1</td></tr><tr><td>1</td><td>3, 6, 7</td></tr><tr><td>2</td><td>0, 4, 6</td></tr><tr><td>3</td><td>5, 6, 6, 8</td></tr><tr><td>4</td><td>3, 4, 7</td></tr><tr><td>5</td><td>-</td></tr><tr><td>6</td><td>0, 8</td></tr><tr><td>7</td><td>3, 5, 6</td></tr><tr><td>8</td><td>3, 3, 7</td></tr><tr><td>9</td><td>0, 2, 2, 8, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 76.

Mean: 97.47. Standard deviation: 9.82.

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