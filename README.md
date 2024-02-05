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
| <table><tr><td>Date</td><td>05-02-2024</td></tr><tr><td>Special</td><td>69876</td></tr><tr><td>First</td><td>47161</td></tr><tr><td>Second</td><td>54779, 83038</td></tr><tr><td rowspan="2">Third</td><td>54035, 40526, 22723</td></tr><tr><td>04016, 92542, 30851</td></tr><tr><td>Fourth</td><td>1932, 1071, 3559, 6332</td></tr><tr><td rowspan="2">Fifth</td><td>2140, 4907, 6780</td></tr><tr><td>8375, 6102, 2349</td></tr><tr><td>Sixth</td><td>806, 060, 590</td></tr><tr><td>Seventh</td><td>07, 35, 81, 22</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 6, 7, 7</td></tr><tr><td>1</td><td>6</td></tr><tr><td>2</td><td>2, 3, 6</td></tr><tr><td>3</td><td>2, 2, 5, 5, 8</td></tr><tr><td>4</td><td>0, 2, 9</td></tr><tr><td>5</td><td>1, 9</td></tr><tr><td>6</td><td>0, 1</td></tr><tr><td>7</td><td>1, 5, 6, 9</td></tr><tr><td>8</td><td>0, 1</td></tr><tr><td>9</td><td>0</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 125. Min: 81.

Mean: 98.55. Standard deviation: 9.17.

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