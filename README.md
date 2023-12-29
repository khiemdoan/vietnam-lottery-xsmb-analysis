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
| <table><tr><td>Date</td><td>29-12-2023</td></tr><tr><td>Special</td><td>36120</td></tr><tr><td>First</td><td>01808</td></tr><tr><td>Second</td><td>24143, 89224</td></tr><tr><td rowspan="2">Third</td><td>54587, 09307, 57960</td></tr><tr><td>57721, 39016, 39494</td></tr><tr><td>Fourth</td><td>5586, 6574, 7750, 5640</td></tr><tr><td rowspan="2">Fifth</td><td>1559, 8201, 7221</td></tr><tr><td>9586, 8938, 6743</td></tr><tr><td>Sixth</td><td>847, 456, 145</td></tr><tr><td>Seventh</td><td>95, 93, 85, 84</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 7, 8</td></tr><tr><td>1</td><td>6</td></tr><tr><td>2</td><td>0, 1, 1, 4</td></tr><tr><td>3</td><td>8</td></tr><tr><td>4</td><td>0, 3, 3, 5, 7</td></tr><tr><td>5</td><td>0, 6, 9</td></tr><tr><td>6</td><td>0</td></tr><tr><td>7</td><td>4</td></tr><tr><td>8</td><td>4, 5, 6, 6, 7</td></tr><tr><td>9</td><td>3, 4, 5</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 130. Min: 78.

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