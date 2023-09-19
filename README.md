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
| <table><tr><td>Date</td><td>19-09-2023</td></tr><tr><td>Special</td><td>50925</td></tr><tr><td>First</td><td>75781</td></tr><tr><td>Second</td><td>95072, 45895</td></tr><tr><td rowspan="2">Third</td><td>41571, 89042, 12852</td></tr><tr><td>47456, 00818, 62562</td></tr><tr><td>Fourth</td><td>8894, 5615, 3165, 5278</td></tr><tr><td rowspan="2">Fifth</td><td>1942, 7055, 3612</td></tr><tr><td>4780, 5138, 3630</td></tr><tr><td>Sixth</td><td>212, 766, 598</td></tr><tr><td>Seventh</td><td>41, 28, 85, 40</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>2, 2, 5, 8</td></tr><tr><td>2</td><td>5, 8</td></tr><tr><td>3</td><td>0, 8</td></tr><tr><td>4</td><td>0, 1, 2, 2</td></tr><tr><td>5</td><td>2, 5, 6</td></tr><tr><td>6</td><td>2, 5, 6</td></tr><tr><td>7</td><td>1, 2, 8</td></tr><tr><td>8</td><td>0, 1, 5</td></tr><tr><td>9</td><td>4, 5, 8</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 77.

Mean: 97.47. Standard deviation: 10.01.

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