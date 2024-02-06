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
| <table><tr><td>Date</td><td>06-02-2024</td></tr><tr><td>Special</td><td>91267</td></tr><tr><td>First</td><td>65567</td></tr><tr><td>Second</td><td>49583, 27981</td></tr><tr><td rowspan="2">Third</td><td>28941, 63811, 68505</td></tr><tr><td>68457, 98492, 31709</td></tr><tr><td>Fourth</td><td>1990, 1136, 7461, 6895</td></tr><tr><td rowspan="2">Fifth</td><td>2312, 4696, 2846</td></tr><tr><td>0206, 8873, 3910</td></tr><tr><td>Sixth</td><td>017, 320, 886</td></tr><tr><td>Seventh</td><td>52, 59, 84, 15</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>5, 6, 9</td></tr><tr><td>1</td><td>0, 1, 2, 5, 7</td></tr><tr><td>2</td><td>0</td></tr><tr><td>3</td><td>6</td></tr><tr><td>4</td><td>1, 6</td></tr><tr><td>5</td><td>2, 7, 9</td></tr><tr><td>6</td><td>1, 7, 7</td></tr><tr><td>7</td><td>3</td></tr><tr><td>8</td><td>1, 3, 4, 6</td></tr><tr><td>9</td><td>0, 2, 5, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 80.

Mean: 98.55. Standard deviation: 9.24.

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