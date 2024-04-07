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
| <table><tr><td>Date</td><td>07-04-2024</td></tr><tr><td>Special</td><td>93374</td></tr><tr><td>First</td><td>18300</td></tr><tr><td>Second</td><td>59549, 37037</td></tr><tr><td rowspan="2">Third</td><td>74266, 07569, 23624</td></tr><tr><td>78397, 06513, 35761</td></tr><tr><td>Fourth</td><td>1734, 8632, 0757, 2118</td></tr><tr><td rowspan="2">Fifth</td><td>7324, 2369, 6427</td></tr><tr><td>8196, 1825, 4339</td></tr><tr><td>Sixth</td><td>185, 275, 044</td></tr><tr><td>Seventh</td><td>65, 17, 72, 50</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0</td></tr><tr><td>1</td><td>3, 7, 8</td></tr><tr><td>2</td><td>4, 4, 5, 7</td></tr><tr><td>3</td><td>2, 4, 7, 9</td></tr><tr><td>4</td><td>4, 9</td></tr><tr><td>5</td><td>0, 7</td></tr><tr><td>6</td><td>1, 5, 6, 9, 9</td></tr><tr><td>7</td><td>2, 4, 5</td></tr><tr><td>8</td><td>5</td></tr><tr><td>9</td><td>6, 7</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 73.

Mean: 97.74. Standard deviation: 9.19.

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