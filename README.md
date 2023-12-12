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
| <table><tr><td>Date</td><td>12-12-2023</td></tr><tr><td>Special</td><td>62970</td></tr><tr><td>First</td><td>39467</td></tr><tr><td>Second</td><td>40628, 04048</td></tr><tr><td rowspan="2">Third</td><td>85828, 50051, 17798</td></tr><tr><td>87941, 64115, 64474</td></tr><tr><td>Fourth</td><td>6711, 8324, 0621, 5607</td></tr><tr><td rowspan="2">Fifth</td><td>1058, 6146, 6328</td></tr><tr><td>5593, 5917, 7918</td></tr><tr><td>Sixth</td><td>954, 545, 397</td></tr><tr><td>Seventh</td><td>63, 29, 28, 51</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>7</td></tr><tr><td>1</td><td>1, 5, 7, 8</td></tr><tr><td>2</td><td>1, 4, 8, 8, 8, 8, 9</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>1, 5, 6, 8</td></tr><tr><td>5</td><td>1, 1, 4, 8</td></tr><tr><td>6</td><td>3, 7</td></tr><tr><td>7</td><td>0, 4</td></tr><tr><td>8</td><td>-</td></tr><tr><td>9</td><td>3, 7, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 129. Min: 76.

Mean: 97.47. Standard deviation: 9.41.

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