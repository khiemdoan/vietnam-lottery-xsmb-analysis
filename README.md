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
| <table><tr><td>Date</td><td>07-11-2023</td></tr><tr><td>Special</td><td>10949</td></tr><tr><td>First</td><td>97813</td></tr><tr><td>Second</td><td>40248, 97258</td></tr><tr><td rowspan="2">Third</td><td>17172, 53726, 16571</td></tr><tr><td>15018, 50843, 54542</td></tr><tr><td>Fourth</td><td>2387, 7105, 7024, 0996</td></tr><tr><td rowspan="2">Fifth</td><td>8370, 7910, 5928</td></tr><tr><td>1004, 2693, 8577</td></tr><tr><td>Sixth</td><td>045, 513, 973</td></tr><tr><td>Seventh</td><td>27, 90, 24, 03</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>3, 4, 5</td></tr><tr><td>1</td><td>0, 3, 3, 8</td></tr><tr><td>2</td><td>4, 4, 6, 7, 8</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>2, 3, 5, 8, 9</td></tr><tr><td>5</td><td>8</td></tr><tr><td>6</td><td>-</td></tr><tr><td>7</td><td>0, 1, 2, 3, 7</td></tr><tr><td>8</td><td>7</td></tr><tr><td>9</td><td>0, 3, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 127. Min: 77.

Mean: 97.47. Standard deviation: 9.1.

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