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
| <table><tr><td>Date</td><td>29-08-2023</td></tr><tr><td>Special</td><td>49278</td></tr><tr><td>First</td><td>26681</td></tr><tr><td>Second</td><td>25277, 61276</td></tr><tr><td rowspan="2">Third</td><td>25040, 04826, 77227</td></tr><tr><td>44526, 16626, 06494</td></tr><tr><td>Fourth</td><td>1586, 5687, 6866, 2962</td></tr><tr><td rowspan="2">Fifth</td><td>6617, 6686, 1073</td></tr><tr><td>9124, 8961, 3505</td></tr><tr><td>Sixth</td><td>030, 130, 681</td></tr><tr><td>Seventh</td><td>22, 72, 21, 71</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>5</td></tr><tr><td>1</td><td>7</td></tr><tr><td>2</td><td>1, 2, 4, 6, 6, 6, 7</td></tr><tr><td>3</td><td>0, 0</td></tr><tr><td>4</td><td>0</td></tr><tr><td>5</td><td>-</td></tr><tr><td>6</td><td>1, 2, 6</td></tr><tr><td>7</td><td>1, 2, 3, 6, 7, 8</td></tr><tr><td>8</td><td>1, 1, 6, 6, 7</td></tr><tr><td>9</td><td>4</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 123. Min: 78.

Mean: 97.47. Standard deviation: 10.21.

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