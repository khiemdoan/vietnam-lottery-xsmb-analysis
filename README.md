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
| <table><tr><td>Date</td><td>07-02-2024</td></tr><tr><td>Special</td><td>67384</td></tr><tr><td>First</td><td>41504</td></tr><tr><td>Second</td><td>84043, 71031</td></tr><tr><td rowspan="2">Third</td><td>23490, 95377, 73674</td></tr><tr><td>51711, 88162, 69864</td></tr><tr><td>Fourth</td><td>9296, 1005, 2278, 5705</td></tr><tr><td rowspan="2">Fifth</td><td>2043, 7662, 9506</td></tr><tr><td>3669, 1073, 3804</td></tr><tr><td>Sixth</td><td>638, 152, 189</td></tr><tr><td>Seventh</td><td>62, 18, 99, 53</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>4, 4, 5, 5, 6</td></tr><tr><td>1</td><td>1, 8</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>1, 8</td></tr><tr><td>4</td><td>3, 3</td></tr><tr><td>5</td><td>2, 3</td></tr><tr><td>6</td><td>2, 2, 2, 4, 9</td></tr><tr><td>7</td><td>3, 4, 7, 8</td></tr><tr><td>8</td><td>4, 9</td></tr><tr><td>9</td><td>0, 6, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 81.

Mean: 98.55. Standard deviation: 9.23.

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