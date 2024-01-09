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
| <table><tr><td>Date</td><td>09-01-2024</td></tr><tr><td>Special</td><td>48877</td></tr><tr><td>First</td><td>34321</td></tr><tr><td>Second</td><td>62959, 65902</td></tr><tr><td rowspan="2">Third</td><td>26683, 31049, 98561</td></tr><tr><td>68229, 37571, 53782</td></tr><tr><td>Fourth</td><td>0360, 5370, 3054, 4853</td></tr><tr><td rowspan="2">Fifth</td><td>4143, 7962, 1775</td></tr><tr><td>2023, 0455, 3683</td></tr><tr><td>Sixth</td><td>287, 175, 670</td></tr><tr><td>Seventh</td><td>77, 68, 08, 91</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 8</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>1, 3, 9</td></tr><tr><td>3</td><td>-</td></tr><tr><td>4</td><td>3, 9</td></tr><tr><td>5</td><td>3, 4, 5, 9</td></tr><tr><td>6</td><td>0, 1, 2, 8</td></tr><tr><td>7</td><td>0, 0, 1, 5, 5, 7, 7</td></tr><tr><td>8</td><td>2, 3, 3, 7</td></tr><tr><td>9</td><td>1</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 126. Min: 78.

Mean: 97.47. Standard deviation: 9.35.

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