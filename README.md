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
| <table><tr><td>Date</td><td>10-03-2023</td></tr><tr><td>Special</td><td>24420</td></tr><tr><td>First</td><td>64647</td></tr><tr><td>Second</td><td>92456, 73117</td></tr><tr><td rowspan="2">Third</td><td>43430, 17679, 18857</td></tr><tr><td>58788, 06086, 56612</td></tr><tr><td>Fourth</td><td>6449, 3646, 0895, 3184</td></tr><tr><td rowspan="2">Fifth</td><td>9301, 4549, 8069</td></tr><tr><td>7225, 3674, 8235</td></tr><tr><td>Sixth</td><td>810, 645, 849</td></tr><tr><td>Seventh</td><td>97, 07, 58, 81</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 7</td></tr><tr><td>1</td><td>0, 2, 7</td></tr><tr><td>2</td><td>0, 5</td></tr><tr><td>3</td><td>0, 5</td></tr><tr><td>4</td><td>5, 6, 7, 9, 9, 9</td></tr><tr><td>5</td><td>6, 7, 8</td></tr><tr><td>6</td><td>9</td></tr><tr><td>7</td><td>4, 9</td></tr><tr><td>8</td><td>1, 4, 6, 8</td></tr><tr><td>9</td><td>5, 7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 124. Min: 75.

Mean: 97.47. Standard deviation: 11.55.

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