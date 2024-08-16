# Vietnam Lottery (XSMB) Analysis

Using GitHub Action to automatically fetch and analyze results of the Vietnam lottery daily.

Sử dụng GitHub Action để tự động hoá thu thập và phân tích kết quả xổ số hàng ngày của Việt Nam.

Download:

* [Full data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb.csv)
* [1-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_1_year.csv)
* [2-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_2_year.csv)
* [3-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_3_year.csv)
* [5-year data](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/main/results/xsmb_5_year.csv)

| Lottery (Xổ số) | Loto (Lô tô) |
| :------------: | :----------: |
| <table><tr><td>Date (Ngày)</td><td>16-08-2024</td></tr><tr><td>Special (Giải dặc biệt)</td><td>82327</td></tr><tr><td>First (Giải nhất)</td><td>87207</td></tr><tr><td>Second (Giải nhì)</td><td>58978, 66424</td></tr><tr><td rowspan="2">Third (Giải ba)</td><td>52741, 48515, 03307</td></tr><tr><td>35681, 46004, 06090</td></tr><tr><td>Fourth (Giải tư)</td><td>0938, 1704, 1997, 5256</td></tr><tr><td rowspan="2">Fifth (Giải năm)</td><td>9835, 3221, 3558</td></tr><tr><td>7606, 0420, 9829</td></tr><tr><td>Sixth (Giải sáu)</td><td>274, 577, 200</td></tr><tr><td>Seventh (Giải bảy)</td><td>32, 65, 12, 52</td></tr></table> | <table><tr><td>First (Đầu)</td><td>Last (Đuôi)</td></tr><tr><td>0</td><td>0, 4, 4, 6, 7, 7</td></tr><tr><td>1</td><td>2, 5</td></tr><tr><td>2</td><td>0, 1, 4, 7, 9</td></tr><tr><td>3</td><td>2, 5, 8</td></tr><tr><td>4</td><td>1</td></tr><tr><td>5</td><td>2, 6, 8</td></tr><tr><td>6</td><td>5</td></tr><tr><td>7</td><td>4, 7, 8</td></tr><tr><td>8</td><td>1</td></tr><tr><td>9</td><td>0, 7</td></tr></table> |

<details>
  <summary><h2>Analysis of special prices (Phân tích kết quả xổ số)</h2></summary>
  <h3>Amount of day from last appearing (Số ngày từ lần xuất hiện cuối cùng)</h3>

  ![Delta](images/special_delta.jpg)

  <h3>Top 10 amount of day from last appearing (Top 10 số lâu chưa xuất hiện)</h3>

  ![Delta top 10](images/special_delta_top_10.jpg)
</details>

<details>
  <summary><h2>Analysis of one-year Loto results (Phân tích kết quả lô tô trong 1 năm)</h2></summary>

  Max: 130. Min: 66.

  Mean: 97.74. Standard deviation: 11.68.

  <h3>Detail (Chi tiết)</h3>

  ![Detail](images/heatmap.jpg)

  <h3>Top 10</h3>

  ![Top 10](images/top-10.jpg)

  <h3>Distribution (Phân bổ)</h3>

  ![Distribution](images/distribution.jpg)
</details>

<details>
  <summary><h3>Amount of day from last appearing (Số ngày từ lần xuất hiện cưới cùng)</h2></summary>

  ![Delta](images/delta.jpg)

  <h3>Top 10 amount of day from last appearing (Top 10 số lâu chưa xuất hiện)</h3>

  ![Delta top 10](images/delta_top_10.jpg)
</details>