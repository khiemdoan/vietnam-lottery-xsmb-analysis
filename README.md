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
| <table><tr><td>Date</td><td>18-01-2024</td></tr><tr><td>Special</td><td>54998</td></tr><tr><td>First</td><td>54578</td></tr><tr><td>Second</td><td>92914, 81659</td></tr><tr><td rowspan="2">Third</td><td>67486, 76176, 28243</td></tr><tr><td>25690, 97325, 27064</td></tr><tr><td>Fourth</td><td>0717, 5736, 1747, 7684</td></tr><tr><td rowspan="2">Fifth</td><td>3998, 8610, 3999</td></tr><tr><td>4749, 8700, 9998</td></tr><tr><td>Sixth</td><td>933, 271, 914</td></tr><tr><td>Seventh</td><td>77, 23, 11, 48</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>0</td></tr><tr><td>1</td><td>0, 1, 4, 4, 7</td></tr><tr><td>2</td><td>3, 5</td></tr><tr><td>3</td><td>3, 6</td></tr><tr><td>4</td><td>3, 7, 8, 9</td></tr><tr><td>5</td><td>9</td></tr><tr><td>6</td><td>4</td></tr><tr><td>7</td><td>1, 6, 7, 8</td></tr><tr><td>8</td><td>4, 6</td></tr><tr><td>9</td><td>0, 8, 8, 8, 9</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 122. Min: 80.

Mean: 97.47. Standard deviation: 8.73.

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