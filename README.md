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
| <table><tr><td>Date</td><td>17-11-2023</td></tr><tr><td>Special</td><td>95110</td></tr><tr><td>First</td><td>91230</td></tr><tr><td>Second</td><td>25848, 37352</td></tr><tr><td rowspan="2">Third</td><td>46596, 92391, 75545</td></tr><tr><td>86395, 28746, 58992</td></tr><tr><td>Fourth</td><td>7879, 2244, 9001, 6647</td></tr><tr><td rowspan="2">Fifth</td><td>4782, 2335, 0826</td></tr><tr><td>9117, 2981, 5762</td></tr><tr><td>Sixth</td><td>366, 704, 757</td></tr><tr><td>Seventh</td><td>38, 44, 68, 52</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 4</td></tr><tr><td>1</td><td>0, 7</td></tr><tr><td>2</td><td>6</td></tr><tr><td>3</td><td>0, 5, 8</td></tr><tr><td>4</td><td>4, 4, 5, 6, 7, 8</td></tr><tr><td>5</td><td>2, 2, 7</td></tr><tr><td>6</td><td>2, 6, 8</td></tr><tr><td>7</td><td>9</td></tr><tr><td>8</td><td>1, 2</td></tr><tr><td>9</td><td>1, 2, 5, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 129. Min: 77.

Mean: 97.47. Standard deviation: 9.57.

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