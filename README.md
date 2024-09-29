# Vietnam Lottery (XSMB) Analysis

Using GitHub Action to automatically fetch and analyze results of the Vietnam lottery daily.

Sử dụng GitHub Action để tự động hoá thu thập và phân tích kết quả xổ số hàng ngày của Việt Nam.

This project is created by [Khiem Doan](https://github.com/khiemdoan). I create this project for education purpose only. You can use any resource in this repository for free without any permission.

Dự án này được tạo bởi [Khiêm Đoàn](https://github.com/khiemdoan). Tôi tạo dự án này chỉ nhằm mục đích học tập. Bạn có thể sử dụng bất kỳ tài nguyên nào trong kho lưu trữ này một cách miễn phí mà không cần bất kỳ sự cho phép nào.

## Data (Dữ liệu)

* Raw data: [xsmb.csv](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb.csv) [xsmb.json](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb.json)
* 2-digits data: [xsmb-2-digits.csv](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-2-digits.csv) [xsmb-2-digits.json](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-2-digits.json)
* Sparse data: [xsmb-sparse.csv](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-sparse.csv) [xsmb-sparse.json](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-sparse.json)

| Lottery (Xổ số) | Loto (Lô tô) |
| :------------: | :----------: |
| <table><tr><td>Date (Ngày)</td><td>29-09-2024</td></tr><tr><td>Special (Giải đặc biệt)</td><td>76086</td></tr><tr><td>First (Giải nhất)</td><td>05076</td></tr><tr><td>Second (Giải nhì)</td><td>86459, 72177</td></tr><tr><td rowspan="2">Third (Giải ba)</td><td>02516, 92166, 41540</td></tr><tr><td>13840, 30112, 37013</td></tr><tr><td>Fourth (Giải tư)</td><td>1435, 4391, 3249, 8117</td></tr><tr><td rowspan="2">Fifth (Giải năm)</td><td>4539, 9727, 5882</td></tr><tr><td>6093, 3496, 2522</td></tr><tr><td>Sixth (Giải sáu)</td><td>237, 862, 310</td></tr><tr><td>Seventh (Giải bảy)</td><td>67, 22, 86, 29</td></tr></table> | <table><tr><td>First (Đầu)</td><td>Last (Đuôi)</td></tr><tr><td>0</td><td>-</td></tr><tr><td>1</td><td>0, 2, 3, 6, 7</td></tr><tr><td>2</td><td>2, 2, 7, 9</td></tr><tr><td>3</td><td>5, 7, 9</td></tr><tr><td>4</td><td>0, 0, 9</td></tr><tr><td>5</td><td>9</td></tr><tr><td>6</td><td>2, 6, 7</td></tr><tr><td>7</td><td>6, 7</td></tr><tr><td>8</td><td>2, 6, 6</td></tr><tr><td>9</td><td>1, 3, 6</td></tr></table> |

<details>
  <summary><h2>Analysis of special prices (Phân tích kết quả xổ số)</h2></summary>
  <h3>Amount of day from last appearing (Số ngày từ lần xuất hiện cuối cùng)</h3>

  ![Delta](images/special_delta.jpg)

  <h3>Top 10 amount of day from last appearing (Top 10 số lâu chưa xuất hiện)</h3>

  ![Delta top 10](images/special_delta_top_10.jpg)
</details>

<details>
  <summary><h2>Analysis of one-year Loto results (Phân tích kết quả lô tô trong 1 năm)</h2></summary>

  Max: 130. Min: 63.

  Mean: 97.74. Standard deviation: 11.91.

  <h3>Detail (Chi tiết)</h3>

  ![Detail](images/heatmap.jpg)

  <h3>Top 10</h3>

  ![Top 10](images/top-10.jpg)

  <h3>Distribution (Phân bổ)</h3>

  ![Distribution](images/distribution.jpg)
</details>

<details>
  <summary><h3>Amount of day from last appearing (Số ngày từ lần xuất hiện cuối cùng)</h2></summary>

  ![Delta](images/delta.jpg)

  <h3>Top 10 amount of day from last appearing (Top 10 số lâu chưa xuất hiện)</h3>

  ![Delta top 10](images/delta_top_10.jpg)
</details>