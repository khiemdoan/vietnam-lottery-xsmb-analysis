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
| <table><tr><td>Date</td><td>28-03-2024</td></tr><tr><td>Special</td><td>49879</td></tr><tr><td>First</td><td>61196</td></tr><tr><td>Second</td><td>55813, 26560</td></tr><tr><td rowspan="2">Third</td><td>66628, 39458, 53044</td></tr><tr><td>66883, 94985, 04961</td></tr><tr><td>Fourth</td><td>0689, 1252, 7970, 1626</td></tr><tr><td rowspan="2">Fifth</td><td>4095, 9503, 8586</td></tr><tr><td>7026, 3491, 4985</td></tr><tr><td>Sixth</td><td>800, 015, 450</td></tr><tr><td>Seventh</td><td>07, 82, 98, 90</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 3, 7</td></tr><tr><td>1</td><td>3, 5</td></tr><tr><td>2</td><td>6, 6, 8</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>4</td></tr><tr><td>5</td><td>0, 2, 8</td></tr><tr><td>6</td><td>0, 1</td></tr><tr><td>7</td><td>0, 9</td></tr><tr><td>8</td><td>2, 3, 5, 5, 6, 9</td></tr><tr><td>9</td><td>0, 1, 5, 6, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 121. Min: 76.

Mean: 97.74. Standard deviation: 8.96.

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