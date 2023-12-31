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
| <table><tr><td>Date</td><td>31-12-2023</td></tr><tr><td>Special</td><td>73758</td></tr><tr><td>First</td><td>80689</td></tr><tr><td>Second</td><td>75152, 42067</td></tr><tr><td rowspan="2">Third</td><td>69905, 79800, 28338</td></tr><tr><td>29736, 28168, 24917</td></tr><tr><td>Fourth</td><td>3277, 9831, 1686, 1236</td></tr><tr><td rowspan="2">Fifth</td><td>2848, 6743, 8909</td></tr><tr><td>8565, 2489, 7595</td></tr><tr><td>Sixth</td><td>292, 586, 465</td></tr><tr><td>Seventh</td><td>42, 82, 02, 43</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0, 2, 5, 9</td></tr><tr><td>1</td><td>7</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>1, 6, 6, 8</td></tr><tr><td>4</td><td>2, 3, 3, 8</td></tr><tr><td>5</td><td>2, 8</td></tr><tr><td>6</td><td>5, 5, 7, 8</td></tr><tr><td>7</td><td>7</td></tr><tr><td>8</td><td>2, 6, 6, 9, 9</td></tr><tr><td>9</td><td>2, 5</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 129. Min: 79.

Mean: 97.47. Standard deviation: 9.45.

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