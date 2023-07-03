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
| <table><tr><td>Date</td><td>03-07-2023</td></tr><tr><td>Special</td><td>96894</td></tr><tr><td>First</td><td>03260</td></tr><tr><td>Second</td><td>17064, 71834</td></tr><tr><td rowspan="2">Third</td><td>86082, 55306, 22767</td></tr><tr><td>85062, 06138, 27224</td></tr><tr><td>Fourth</td><td>6983, 2670, 2483, 7136</td></tr><tr><td rowspan="2">Fifth</td><td>7354, 5524, 1596</td></tr><tr><td>1151, 3202, 4001</td></tr><tr><td>Sixth</td><td>005, 551, 305</td></tr><tr><td>Seventh</td><td>49, 08, 10, 05</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>1, 2, 5, 5, 5, 6, 8</td></tr><tr><td>1</td><td>0</td></tr><tr><td>2</td><td>4, 4</td></tr><tr><td>3</td><td>4, 6, 8</td></tr><tr><td>4</td><td>9</td></tr><tr><td>5</td><td>1, 1, 4</td></tr><tr><td>6</td><td>0, 2, 4, 7</td></tr><tr><td>7</td><td>0</td></tr><tr><td>8</td><td>2, 3, 3</td></tr><tr><td>9</td><td>4, 6</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 128. Min: 75.

Mean: 97.47. Standard deviation: 9.95.

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