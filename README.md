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
| <table><tr><td>Date</td><td>31-01-2024</td></tr><tr><td>Special</td><td>47666</td></tr><tr><td>First</td><td>58427</td></tr><tr><td>Second</td><td>64931, 25644</td></tr><tr><td rowspan="2">Third</td><td>03576, 08099, 93000</td></tr><tr><td>05237, 32951, 82863</td></tr><tr><td>Fourth</td><td>3767, 5450, 1997, 6766</td></tr><tr><td rowspan="2">Fifth</td><td>1336, 0386, 7369</td></tr><tr><td>1740, 4840, 8051</td></tr><tr><td>Sixth</td><td>296, 125, 966</td></tr><tr><td>Seventh</td><td>68, 53, 82, 27</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>5, 7, 7</td></tr><tr><td>3</td><td>1, 6, 7</td></tr><tr><td>4</td><td>0, 0, 4</td></tr><tr><td>5</td><td>0, 1, 1, 3</td></tr><tr><td>6</td><td>3, 6, 6, 6, 7, 8, 9</td></tr><tr><td>7</td><td>6</td></tr><tr><td>8</td><td>2, 6</td></tr><tr><td>9</td><td>6, 7, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 82.

Mean: 98.55. Standard deviation: 8.87.

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