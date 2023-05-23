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
| <table><tr><td>Date</td><td>23-05-2023</td></tr><tr><td>Special</td><td>95972</td></tr><tr><td>First</td><td>02366</td></tr><tr><td>Second</td><td>43590, 56621</td></tr><tr><td rowspan="2">Third</td><td>19195, 14216, 52782</td></tr><tr><td>53347, 92819, 99789</td></tr><tr><td>Fourth</td><td>0740, 6907, 5957, 8967</td></tr><tr><td rowspan="2">Fifth</td><td>4851, 8691, 5830</td></tr><tr><td>7301, 6230, 3908</td></tr><tr><td>Sixth</td><td>882, 890, 258</td></tr><tr><td>Seventh</td><td>61, 27, 17, 44</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 7, 8</td></tr><tr><td>1</td><td>6, 7, 9</td></tr><tr><td>2</td><td>1, 7</td></tr><tr><td>3</td><td>0, 0</td></tr><tr><td>4</td><td>0, 4, 7</td></tr><tr><td>5</td><td>1, 7, 8</td></tr><tr><td>6</td><td>1, 6, 7</td></tr><tr><td>7</td><td>2</td></tr><tr><td>8</td><td>2, 2, 9</td></tr><tr><td>9</td><td>0, 0, 1, 5</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 121. Min: 75.

Mean: 97.47. Standard deviation: 10.46.

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