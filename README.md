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
| <table><tr><td>Date</td><td>26-07-2023</td></tr><tr><td>Special</td><td>87929</td></tr><tr><td>First</td><td>75634</td></tr><tr><td>Second</td><td>97192, 60780</td></tr><tr><td rowspan="2">Third</td><td>91837, 73432, 89201</td></tr><tr><td>03500, 17989, 38853</td></tr><tr><td>Fourth</td><td>6924, 2208, 9694, 8150</td></tr><tr><td rowspan="2">Fifth</td><td>2455, 2219, 3159</td></tr><tr><td>5163, 3656, 1122</td></tr><tr><td>Sixth</td><td>017, 021, 657</td></tr><tr><td>Seventh</td><td>64, 60, 08, 94</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 1, 8, 8</td></tr><tr><td>1</td><td>7, 9</td></tr><tr><td>2</td><td>1, 2, 4, 9</td></tr><tr><td>3</td><td>2, 4, 7</td></tr><tr><td>4</td><td>-</td></tr><tr><td>5</td><td>0, 3, 5, 6, 7, 9</td></tr><tr><td>6</td><td>0, 3, 4</td></tr><tr><td>7</td><td>-</td></tr><tr><td>8</td><td>0, 9</td></tr><tr><td>9</td><td>2, 4, 4</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 129. Min: 75.

Mean: 97.47. Standard deviation: 10.04.

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