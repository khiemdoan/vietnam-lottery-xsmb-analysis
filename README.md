# Vietnam Lottery (XSMB) Analysis

Using GitHub Action to automatically fetch and analyze results of the Vietnam lottery daily.

This project is created by [Khiem Doan](https://github.com/khiemdoan). I create this project for education purpose only. You can use any resource in this repository for free without any permission.

Sử dụng GitHub Action để tự động hoá thu thập và phân tích kết quả xổ số hàng ngày của Việt Nam.

Dự án này được tạo bởi [Khiêm Đoàn](https://github.com/khiemdoan). Tôi tạo dự án này chỉ nhằm mục đích học tập. Bạn có thể sử dụng bất kỳ tài nguyên nào trong kho lưu trữ này một cách miễn phí mà không cần bất kỳ sự cho phép nào.

| Lottery (Xổ số) | Loto (Lô tô) |
| :------------: | :----------: |
| <table><tr><td>Date (Ngày)</td><td>28-05-2025</td></tr><tr><td>Special (Giải đặc biệt)</td><td>27634</td></tr><tr><td>First (Giải nhất)</td><td>95953</td></tr><tr><td>Second (Giải nhì)</td><td>63828, 88926</td></tr><tr><td rowspan="2">Third (Giải ba)</td><td>10330, 72375, 95416</td></tr><tr><td>06622, 41822, 64937</td></tr><tr><td>Fourth (Giải tư)</td><td>3203, 3000, 8254, 8382</td></tr><tr><td rowspan="2">Fifth (Giải năm)</td><td>4169, 6955, 4558</td></tr><tr><td>8003, 0529, 0358</td></tr><tr><td>Sixth (Giải sáu)</td><td>984, 873, 568</td></tr><tr><td>Seventh (Giải bảy)</td><td>52, 33, 98, 37</td></tr></table> | <table><tr><td>First (Đầu)</td><td>Last (Đuôi)</td></tr><tr><td>0</td><td>0, 3, 3</td></tr><tr><td>1</td><td>6</td></tr><tr><td>2</td><td>2, 2, 6, 8, 9</td></tr><tr><td>3</td><td>0, 3, 4, 7, 7</td></tr><tr><td>4</td><td>-</td></tr><tr><td>5</td><td>2, 3, 4, 5, 8, 8</td></tr><tr><td>6</td><td>8, 9</td></tr><tr><td>7</td><td>3, 5</td></tr><tr><td>8</td><td>2, 4</td></tr><tr><td>9</td><td>8</td></tr></table> |

## Data (Dữ liệu)

* Raw data: [xsmb.csv](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb.csv) [xsmb.json](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb.json)
* 2-digits data: [xsmb-2-digits.csv](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-2-digits.csv) [xsmb-2-digits.json](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-2-digits.json)
* Sparse data: [xsmb-sparse.csv](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-sparse.csv) [xsmb-sparse.json](https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-sparse.json)

## Using

You can use `curl` or `wget` to download data files. Or you can load them directly into DataFrame:

Bạn có thể sử dụng curl hoặc wget để tải các tệp dữ liệu. Hoặc bạn có thể tải chúng trực tiếp vào DataFrame:

```sh
wget https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb.csv
```

```sh
curl -O https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-2-digits.csv
```

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/khiemdoan/vietnam-lottery-xsmb-analysis/refs/heads/main/data/xsmb-sparse.csv')
df.info()
```

<details>
  <summary><h2>Analysis of special prices (Phân tích kết quả xổ số)</h2></summary>
  <h3>Amount of day from last appearing (Số ngày từ lần xuất hiện cuối cùng)</h3>

  ![Delta](images/special_delta.jpg)

  <h3>Top 10 amount of day from last appearing (Top 10 số lâu chưa xuất hiện)</h3>

  ![Delta top 10](images/special_delta_top_10.jpg)
</details>

<details>
  <summary><h2>Analysis of one-year Loto results (Phân tích kết quả lô tô trong 1 năm)</h2></summary>

  Max: 122. Min: 67.

  Mean: 97.47. Standard deviation: 9.85.

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