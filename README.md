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
| <table><tr><td>Date</td><td>11-03-2023</td></tr><tr><td>Special</td><td>47076</td></tr><tr><td>First</td><td>91911</td></tr><tr><td>Second</td><td>68062, 89887</td></tr><tr><td rowspan="2">Third</td><td>97745, 08606, 90078</td></tr><tr><td>48492, 59226, 23122</td></tr><tr><td>Fourth</td><td>1723, 6001, 7707, 8139</td></tr><tr><td rowspan="2">Fifth</td><td>9794, 4226, 2120</td></tr><tr><td>7005, 9711, 9405</td></tr><tr><td>Sixth</td><td>880, 643, 489</td></tr><tr><td>Seventh</td><td>08, 68, 94, 48</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 5, 5, 6, 7, 8</td></tr><tr><td>1</td><td>1, 1</td></tr><tr><td>2</td><td>0, 2, 3, 6, 6</td></tr><tr><td>3</td><td>9</td></tr><tr><td>4</td><td>3, 5, 8</td></tr><tr><td>5</td><td>-</td></tr><tr><td>6</td><td>2, 8</td></tr><tr><td>7</td><td>6, 8</td></tr><tr><td>8</td><td>0, 7, 9</td></tr><tr><td>9</td><td>2, 4, 4</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 75.

Mean: 97.47. Standard deviation: 11.48.

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