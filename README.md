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
| <table><tr><td>Date</td><td>30-06-2023</td></tr><tr><td>Special</td><td>69851</td></tr><tr><td>First</td><td>88124</td></tr><tr><td>Second</td><td>66159, 11919</td></tr><tr><td rowspan="2">Third</td><td>07922, 80284, 92702</td></tr><tr><td>43791, 92613, 53904</td></tr><tr><td>Fourth</td><td>4262, 5196, 2479, 4379</td></tr><tr><td rowspan="2">Fifth</td><td>2466, 8092, 8630</td></tr><tr><td>6719, 3089, 6022</td></tr><tr><td>Sixth</td><td>207, 869, 283</td></tr><tr><td>Seventh</td><td>89, 82, 08, 34</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 4, 7, 8</td></tr><tr><td>1</td><td>3, 9, 9</td></tr><tr><td>2</td><td>2, 2, 4</td></tr><tr><td>3</td><td>0, 4</td></tr><tr><td>4</td><td>-</td></tr><tr><td>5</td><td>1, 9</td></tr><tr><td>6</td><td>2, 6, 9</td></tr><tr><td>7</td><td>9, 9</td></tr><tr><td>8</td><td>2, 3, 4, 9, 9</td></tr><tr><td>9</td><td>1, 2, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 127. Min: 76.

Mean: 97.47. Standard deviation: 9.81.

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