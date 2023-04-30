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
| <table><tr><td>Date</td><td>30-04-2023</td></tr><tr><td>Special</td><td>90819</td></tr><tr><td>First</td><td>14462</td></tr><tr><td>Second</td><td>46938, 76537</td></tr><tr><td rowspan="2">Third</td><td>64883, 87706, 17676</td></tr><tr><td>03683, 13446, 65386</td></tr><tr><td>Fourth</td><td>6589, 1038, 8701, 2478</td></tr><tr><td rowspan="2">Fifth</td><td>2368, 5706, 7865</td></tr><tr><td>8484, 1913, 5540</td></tr><tr><td>Sixth</td><td>027, 311, 663</td></tr><tr><td>Seventh</td><td>50, 70, 88, 22</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 6, 6</td></tr><tr><td>1</td><td>1, 3, 9</td></tr><tr><td>2</td><td>2, 7</td></tr><tr><td>3</td><td>7, 8, 8</td></tr><tr><td>4</td><td>0, 6</td></tr><tr><td>5</td><td>0</td></tr><tr><td>6</td><td>2, 3, 5, 8</td></tr><tr><td>7</td><td>0, 6, 8</td></tr><tr><td>8</td><td>3, 3, 4, 6, 8, 9</td></tr><tr><td>9</td><td>-</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 122. Min: 75.

Mean: 97.47. Standard deviation: 10.87.

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