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
| <table><tr><td>Date</td><td>16-02-2024</td></tr><tr><td>Special</td><td>34864</td></tr><tr><td>First</td><td>00693</td></tr><tr><td>Second</td><td>97331, 18776</td></tr><tr><td rowspan="2">Third</td><td>56995, 55805, 26599</td></tr><tr><td>22435, 58098, 35835</td></tr><tr><td>Fourth</td><td>8683, 1661, 7450, 8941</td></tr><tr><td rowspan="2">Fifth</td><td>8695, 2954, 6320</td></tr><tr><td>0276, 2666, 1431</td></tr><tr><td>Sixth</td><td>720, 634, 467</td></tr><tr><td>Seventh</td><td>98, 29, 58, 84</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>5</td></tr><tr><td>1</td><td>-</td></tr><tr><td>2</td><td>0, 0, 9</td></tr><tr><td>3</td><td>1, 1, 4, 5, 5</td></tr><tr><td>4</td><td>1</td></tr><tr><td>5</td><td>0, 4, 8</td></tr><tr><td>6</td><td>1, 4, 6, 7</td></tr><tr><td>7</td><td>6, 6</td></tr><tr><td>8</td><td>3, 4</td></tr><tr><td>9</td><td>3, 5, 5, 8, 8, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 121. Min: 79.

Mean: 97.47. Standard deviation: 8.66.

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