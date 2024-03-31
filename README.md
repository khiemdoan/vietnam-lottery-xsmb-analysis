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
| <table><tr><td>Date</td><td>31-03-2024</td></tr><tr><td>Special</td><td>36909</td></tr><tr><td>First</td><td>46217</td></tr><tr><td>Second</td><td>56679, 32203</td></tr><tr><td rowspan="2">Third</td><td>29726, 90557, 54987</td></tr><tr><td>59727, 68447, 57932</td></tr><tr><td>Fourth</td><td>5581, 4902, 3035, 7503</td></tr><tr><td rowspan="2">Fifth</td><td>2059, 7871, 4346</td></tr><tr><td>0991, 7274, 7688</td></tr><tr><td>Sixth</td><td>183, 311, 228</td></tr><tr><td>Seventh</td><td>69, 90, 28, 81</td></tr></table> | <table><tr><td>First</td><td>Last</td></tr><tr><td>0</td><td>2, 3, 3, 9</td></tr><tr><td>1</td><td>1, 7</td></tr><tr><td>2</td><td>6, 7, 8, 8</td></tr><tr><td>3</td><td>2, 5</td></tr><tr><td>4</td><td>6, 7</td></tr><tr><td>5</td><td>7, 9</td></tr><tr><td>6</td><td>9</td></tr><tr><td>7</td><td>1, 4, 9</td></tr><tr><td>8</td><td>1, 1, 3, 7, 8</td></tr><tr><td>9</td><td>0, 1</td></tr></table> |


<h2>Analysis of special prices</h2>

<h3>Amount of day from last appearing</h3>

![Delta](images/special_delta.jpg)

<h3>Top 10 amount of day from last appearing</h3>

![Delta top 10](images/special_delta_top_10.jpg)

<h2>Analysis of one-year results</h2>

Max: 124. Min: 74.

Mean: 97.74. Standard deviation: 9.07.

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