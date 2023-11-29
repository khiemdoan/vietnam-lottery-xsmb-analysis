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
| <table><tr><td>Date</td><td>29-11-2023</td></tr><tr><td>Special</td><td>03141</td></tr><tr><td>First</td><td>42683</td></tr><tr><td>Second</td><td>33410, 77553</td></tr><tr><td rowspan="2">Third</td><td>40459, 27342, 45945</td></tr><tr><td>67889, 05550, 03883</td></tr><tr><td>Fourth</td><td>5665, 3065, 3233, 2570</td></tr><tr><td rowspan="2">Fifth</td><td>8938, 3480, 2573</td></tr><tr><td>5139, 2488, 1808</td></tr><tr><td>Sixth</td><td>378, 618, 017</td></tr><tr><td>Seventh</td><td>05, 90, 42, 87</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>5, 8</td></tr><tr><td>1</td><td>0, 7, 8</td></tr><tr><td>2</td><td>-</td></tr><tr><td>3</td><td>3, 8, 9</td></tr><tr><td>4</td><td>1, 2, 2, 5</td></tr><tr><td>5</td><td>0, 3, 9</td></tr><tr><td>6</td><td>5, 5</td></tr><tr><td>7</td><td>0, 3, 8</td></tr><tr><td>8</td><td>0, 3, 3, 7, 8, 9</td></tr><tr><td>9</td><td>0</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 130. Min: 78.

Mean: 97.47. Standard deviation: 9.66.

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