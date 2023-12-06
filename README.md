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
| <table><tr><td>Date</td><td>06-12-2023</td></tr><tr><td>Special</td><td>93178</td></tr><tr><td>First</td><td>49592</td></tr><tr><td>Second</td><td>64119, 45960</td></tr><tr><td rowspan="2">Third</td><td>32137, 68827, 28080</td></tr><tr><td>32189, 58244, 14627</td></tr><tr><td>Fourth</td><td>7688, 4100, 2489, 4062</td></tr><tr><td rowspan="2">Fifth</td><td>0011, 2061, 5417</td></tr><tr><td>1645, 3408, 5727</td></tr><tr><td>Sixth</td><td>258, 412, 013</td></tr><tr><td>Seventh</td><td>08, 11, 61, 34</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 8, 8</td></tr><tr><td>1</td><td>1, 1, 2, 3, 7, 9</td></tr><tr><td>2</td><td>7, 7, 7</td></tr><tr><td>3</td><td>4, 7</td></tr><tr><td>4</td><td>4, 5</td></tr><tr><td>5</td><td>8</td></tr><tr><td>6</td><td>0, 1, 1, 2</td></tr><tr><td>7</td><td>8</td></tr><tr><td>8</td><td>0, 8, 9, 9</td></tr><tr><td>9</td><td>2</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 130. Min: 77.

Mean: 97.47. Standard deviation: 9.54.

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