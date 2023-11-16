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
| <table><tr><td>Date</td><td>16-11-2023</td></tr><tr><td>Special</td><td>54869</td></tr><tr><td>First</td><td>34677</td></tr><tr><td>Second</td><td>80583, 17410</td></tr><tr><td rowspan="2">Third</td><td>12119, 75379, 69729</td></tr><tr><td>45196, 06463, 06180</td></tr><tr><td>Fourth</td><td>9936, 0565, 5964, 1109</td></tr><tr><td rowspan="2">Fifth</td><td>7356, 9273, 1879</td></tr><tr><td>6015, 4125, 3336</td></tr><tr><td>Sixth</td><td>959, 344, 804</td></tr><tr><td>Seventh</td><td>36, 20, 73, 21</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>4, 9</td></tr><tr><td>1</td><td>0, 5, 9</td></tr><tr><td>2</td><td>0, 1, 5, 9</td></tr><tr><td>3</td><td>6, 6, 6</td></tr><tr><td>4</td><td>4</td></tr><tr><td>5</td><td>6, 9</td></tr><tr><td>6</td><td>3, 4, 5, 9</td></tr><tr><td>7</td><td>3, 3, 7, 9, 9</td></tr><tr><td>8</td><td>0, 3</td></tr><tr><td>9</td><td>6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 129. Min: 76.

Mean: 97.47. Standard deviation: 9.47.

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