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
| <table><tr><td>Date</td><td>01-02-2024</td></tr><tr><td>Special</td><td>87444</td></tr><tr><td>First</td><td>41182</td></tr><tr><td>Second</td><td>94959, 51442</td></tr><tr><td rowspan="2">Third</td><td>93301, 62187, 40592</td></tr><tr><td>47470, 69528, 79028</td></tr><tr><td>Fourth</td><td>7292, 4118, 0777, 5462</td></tr><tr><td rowspan="2">Fifth</td><td>8254, 4416, 2280</td></tr><tr><td>9154, 5079, 9784</td></tr><tr><td>Sixth</td><td>115, 186, 944</td></tr><tr><td>Seventh</td><td>32, 61, 77, 99</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1</td></tr><tr><td>1</td><td>5, 6, 8</td></tr><tr><td>2</td><td>8, 8</td></tr><tr><td>3</td><td>2</td></tr><tr><td>4</td><td>2, 4, 4</td></tr><tr><td>5</td><td>4, 4, 9</td></tr><tr><td>6</td><td>1, 2</td></tr><tr><td>7</td><td>0, 7, 7, 9</td></tr><tr><td>8</td><td>0, 2, 4, 6, 7</td></tr><tr><td>9</td><td>2, 2, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 81.

Mean: 98.55. Standard deviation: 8.9.

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