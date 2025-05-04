# Các import cần thiết cho các hàm còn lại và phần cập nhật dữ liệu
import logging # Mặc dù không dùng trực tiếp trong đoạn này, giữ lại phòng trường hợp Lottery dùng
from datetime import datetime, time, timedelta
from pathlib import Path # Giữ lại phòng trường hợp Lottery dùng hoặc tương lai cần
from time import sleep # Giữ lại phòng trường hợp Lottery dùng

import numpy as np # Cần cho colors_from_values và các hàm last_appearing
import pandas as pd # Cần cho toàn bộ hoạt động
import seaborn as sns # Cần cho các hàm last_appearing
# from jinja2 import Environment, FileSystemLoader, select_autoescape # Không cần nữa vì không tạo README
from matplotlib import pyplot as plt # Cần cho các hàm last_appearing
from pytz import timezone # Cần để xác định ngày fetch

from src.lottery import Lottery


# Hàm này vẫn được giữ lại vì nó không nằm trong phần Analysis bị yêu cầu bỏ
def colors_from_values(values, palette_name):
    # Tránh lỗi chia cho 0 nếu tất cả giá trị bằng nhau
    if max(values) == min(values):
        normalized = np.zeros_like(values)
    else:
        normalized = (values - min(values)) / (max(values) - min(values))

    indices = np.round(normalized * (len(values) - 1)).astype(np.int32)
    # Đảm bảo palette có ít nhất 1 màu
    palette = sns.color_palette(palette_name, max(1, len(values)))
    # Đảm bảo indices không vượt quá giới hạn palette
    indices = np.clip(indices, 0, len(palette) - 1)
    return np.array(palette).take(indices, axis=0)


# Hàm này vẫn được giữ lại vì nó không nằm trong phần Analysis bị yêu cầu bỏ
def last_appearing(data: pd.DataFrame, type: str):
    # Tạo thư mục images nếu chưa tồn tại
    Path('images').mkdir(parents=True, exist_ok=True)

    numbers = data[['special']]
    numbers.reset_index(inplace=True)
    # Kiểm tra nếu numbers rỗng
    if numbers.empty:
        print("Warning: No data found for last_appearing special analysis.")
        return

    predict_index = numbers['index'].max() + 1

    numbers = numbers.melt(id_vars='index', var_name='prize', value_name='value')
    numbers['value'] = numbers['value'] % 100
    last_appearing_series = numbers.groupby(['value'])['index'].max()
    last_appearing_df = last_appearing_series.to_frame()
    last_appearing_df.reset_index(inplace=True) # Đặt lại index để 'value' thành cột
    last_appearing_df['delta'] = predict_index - last_appearing_df['index']
    last_appearing_df.drop('index', axis=1, inplace=True)

    # Điền các số chưa xuất hiện (nếu có) với delta lớn nhất + 1 hoặc một giá trị mặc định lớn
    all_values = pd.DataFrame({'value': range(100)})
    last_appearing_df = pd.merge(all_values, last_appearing_df, on='value', how='left')
    # Giả sử nếu chưa xuất hiện, delta là predict_index (tính từ ngày 0)
    # Hoặc có thể tính bằng predict_index - (-1) nếu index bắt đầu từ 0
    max_delta_observed = last_appearing_df['delta'].max() if not last_appearing_df['delta'].isnull().all() else predict_index
    last_appearing_df['delta'].fillna(max_delta_observed + 1, inplace=True) # Hoặc predict_index

    heatmap_data = last_appearing_df.copy()
    heatmap_data['tens'] = heatmap_data['value'] // 10
    heatmap_data['ones'] = heatmap_data['value'] % 10
    # Sửa pivot để xử lý trường hợp thiếu index/column sau khi merge
    heatmap_data = heatmap_data.pivot_table(index='tens', columns='ones', values='delta', fill_value=heatmap_data['delta'].max()) # fill_value hợp lý hơn là 0
    # Đảm bảo đủ 10 hàng 10 cột
    heatmap_data = heatmap_data.reindex(index=range(10), columns=range(10), fill_value=heatmap_data.max().max()) # fill_value hợp lý
    heatmap_data = heatmap_data.astype(int)

    bar_data = last_appearing_df.sort_values('delta', ascending=False)
    bar_data = bar_data.iloc[:10, :]
    # bar_data.reset_index(inplace=True) # Không cần reset_index vì đã merge trước đó
    # bar_data = bar_data.rename(columns={'index': 'value'}) # Đã có cột 'value'
    bar_data['value_str'] = bar_data['value'].apply(lambda r: f'{r:02d}') # Tạo cột mới cho label

    try:
        fig, ax = plt.subplots()
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn_r', ax=ax) # Đảo ngược cmap có thể hợp lý hơn (đỏ = lâu)
        ax.set_title('Delta Special (Days Since Last Seen)')
        ax.set_xlabel('Ones digit')
        ax.set_ylabel('Tens digit')
        fig.tight_layout()
        fig.savefig('images/special_delta.jpg')
        plt.close(fig) # Đóng figure để giải phóng bộ nhớ

        if not bar_data.empty:
            fig, ax = plt.subplots()
            # palette = reversed(colors_from_values(bar_data['delta'], 'summer')) # reversed không áp dụng trực tiếp cho list
            palette = colors_from_values(bar_data['delta'].values, 'summer_r') # Dùng _r để đảo ngược palette summer
            sns.barplot(data=bar_data, x='value_str', y='delta', hue='value_str', palette=palette, ax=ax, legend=False) # Bỏ hue nếu không cần màu riêng cho từng cột
            # Hoặc dùng dodge=False nếu muốn các cột cùng màu
            # sns.barplot(data=bar_data, x='value_str', y='delta', palette=palette, ax=ax)
            for container in ax.containers:
                ax.bar_label(container, fmt='%d')
            ax.set_title('Top 10 Longest Wait (Special)')
            ax.set_xlabel('Number')
            ax.set_ylabel('Days Since Last Seen')
            fig.tight_layout()
            fig.savefig('images/special_delta_top_10.jpg')
            plt.close(fig) # Đóng figure
        else:
            print("Warning: No data for special top 10 bar chart.")

    except Exception as e:
        print(f"Error plotting special charts: {e}")
        # Đảm bảo đóng plot nếu có lỗi xảy ra giữa chừng
        if 'fig' in locals() and plt.fignum_exists(fig.number):
             plt.close(fig)


# Hàm này vẫn được giữ lại vì nó không nằm trong phần Analysis bị yêu cầu bỏ
def last_appearing_loto(data):
    # Tạo thư mục images nếu chưa tồn tại
    Path('images').mkdir(parents=True, exist_ok=True)

    # Kiểm tra nếu data rỗng
    if data.empty:
        print("Warning: No data found for last_appearing loto analysis.")
        return
    if 'date' not in data.columns:
         print("Warning: 'date' column missing for loto analysis.")
         # Có thể trả về hoặc xử lý khác tùy logic mong muốn
         # return # Bỏ qua nếu thiếu cột date
         numbers = data.copy() # Giả sử không có cột date
         numbers.reset_index(inplace=True)
         id_vars_melt = 'index'
         # Cần index nếu không có date
         if 'index' not in numbers.columns:
              print("Error: Cannot proceed without 'date' or 'index'.")
              return

    else:
         numbers = data.drop('date', axis=1)
         numbers.reset_index(inplace=True)
         id_vars_melt = 'index'


    predict_index = numbers['index'].max() + 1

    # Kiểm tra nếu numbers chỉ còn cột index
    if len(numbers.columns) <= 1:
         print("Warning: No prize columns found for loto analysis after dropping date.")
         return

    numbers = numbers.melt(id_vars=id_vars_melt, var_name='prize', value_name='value')
    # Xử lý giá trị NaN hoặc không phải số trước khi lấy modulo
    numbers = numbers.dropna(subset=['value'])
    numbers = numbers[pd.to_numeric(numbers['value'], errors='coerce').notna()]
    numbers['value'] = numbers['value'].astype(int) % 100

    if numbers.empty:
        print("Warning: No valid numeric prize values found for loto analysis.")
        return

    last_appearing_series = numbers.groupby(['value'])['index'].max()
    last_appearing_df = last_appearing_series.to_frame()
    last_appearing_df.reset_index(inplace=True) # Đặt lại index để 'value' thành cột
    last_appearing_df['delta'] = predict_index - last_appearing_df['index']
    last_appearing_df.drop('index', axis=1, inplace=True)

    # Điền các số chưa xuất hiện (nếu có)
    all_values = pd.DataFrame({'value': range(100)})
    last_appearing_df = pd.merge(all_values, last_appearing_df, on='value', how='left')
    max_delta_observed = last_appearing_df['delta'].max() if not last_appearing_df['delta'].isnull().all() else predict_index
    last_appearing_df['delta'].fillna(max_delta_observed + 1, inplace=True) # Hoặc predict_index

    heatmap_data = last_appearing_df.copy()
    heatmap_data['tens'] = heatmap_data['value'] // 10
    heatmap_data['ones'] = heatmap_data['value'] % 10
    heatmap_data = heatmap_data.pivot_table(index='tens', columns='ones', values='delta', fill_value=heatmap_data['delta'].max())
    heatmap_data = heatmap_data.reindex(index=range(10), columns=range(10), fill_value=heatmap_data.max().max())
    heatmap_data = heatmap_data.astype(int)

    bar_data = last_appearing_df.sort_values('delta', ascending=False)
    bar_data = bar_data.iloc[:10, :]
    bar_data['value_str'] = bar_data['value'].apply(lambda r: f'{r:02d}')

    try:
        fig, ax = plt.subplots()
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='RdYlGn_r', ax=ax) # Đảo ngược cmap
        ax.set_title('Delta Loto (Days Since Last Seen)')
        ax.set_xlabel('Ones digit')
        ax.set_ylabel('Tens digit')
        fig.tight_layout()
        fig.savefig('images/delta.jpg')
        plt.close(fig)

        if not bar_data.empty:
            fig, ax = plt.subplots()
            # palette = reversed(colors_from_values(bar_data['delta'], 'summer'))
            palette = colors_from_values(bar_data['delta'].values, 'summer_r')
            sns.barplot(data=bar_data, x='value_str', y='delta', hue='value_str', palette=palette, ax=ax, legend=False)
            # sns.barplot(data=bar_data, x='value_str', y='delta', palette=palette, ax=ax)
            for container in ax.containers:
                ax.bar_label(container, fmt='%d')
            ax.set_title('Top 10 Longest Wait (Loto)')
            ax.set_xlabel('Number')
            ax.set_ylabel('Days Since Last Seen')
            fig.tight_layout()
            fig.savefig('images/delta_top_10.jpg')
            plt.close(fig)
        else:
             print("Warning: No data for loto top 10 bar chart.")

    except Exception as e:
        print(f"Error plotting loto charts: {e}")
        if 'fig' in locals() and plt.fignum_exists(fig.number):
             plt.close(fig)


if __name__ == '__main__':
    # Cấu hình Pandas (giữ lại vì có thể ảnh hưởng hiệu năng đọc/ghi)
    # Bỏ qua nếu không cài pyarrow hoặc muốn dùng engine mặc định
    try:
        pd.options.io.parquet.engine = 'pyarrow'
        pd.options.mode.string_storage = 'pyarrow'
    except ImportError:
        print("PyArrow not installed, using default Pandas engine/storage.")

    print("Initializing Lottery object...")
    lottery = Lottery()

    print("Loading existing data...")
    try:
        lottery.load()
        print(f"Data loaded. Last date in loaded data: {lottery.get_last_date()}")
    except FileNotFoundError:
        print("Data file not found. Starting fresh or will fetch all required data.")
    except Exception as e:
        print(f"Error loading data: {e}. Proceeding without loaded data.")
        # Có thể khởi tạo lại lottery hoặc các DataFrame của nó ở đây nếu cần

    # --- Download new data ---
    print("Determining date range for fetching new data...")
    try:
        # Lấy ngày cuối cùng từ dữ liệu đã load, nếu load lỗi thì cần xử lý khác
        # Ở đây giả định get_last_date() trả về ngày hợp lệ hoặc ngày hôm nay nếu load lỗi
        begin_date = lottery.get_last_date()
    except Exception as e:
         # Nếu get_last_date() lỗi hoặc chưa có dữ liệu
         print(f"Could not get last date from loaded data ({e}). Setting begin_date to a default (e.g., yesterday).")
         # Cần một ngày mặc định hợp lý, ví dụ 1 ngày trước để fetch ít nhất ngày hôm qua
         begin_date = datetime.now(timezone('Asia/Ho_Chi_Minh')).date() - timedelta(days=1)


    tz = timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)
    last_date_to_fetch = now.date()

    # Chỉ fetch kết quả của ngày hôm qua hoặc trước đó nếu chưa qua giờ quay số
    if now.time() < time(18, 35):
        last_date_to_fetch -= timedelta(days=1)

    print(f"Begin date (exclusive): {begin_date}")
    print(f"Last date to fetch (inclusive): {last_date_to_fetch}")

    # Tính số ngày cần fetch (từ ngày sau begin_date đến hết last_date_to_fetch)
    # Đảm bảo last_date_to_fetch >= begin_date
    if last_date_to_fetch >= begin_date :
        delta_days = (last_date_to_fetch - begin_date).days
        print(f"Need to fetch data for {delta_days} day(s).")

        # Lặp từ ngày ngay sau begin_date đến last_date_to_fetch
        for i in range(1, delta_days + 1): # +1 vì range không bao gồm điểm cuối
            selected_date = begin_date + timedelta(days=i)
            print(f"Fetching data for: {selected_date}")
            try:
                lottery.fetch(selected_date)
                # Có thể thêm sleep nhỏ để tránh làm quá tải server nguồn
                # sleep(0.5) # Ví dụ: nghỉ 0.5 giây
            except Exception as e:
                print(f"Error fetching data for {selected_date}: {e}")
                # Có thể quyết định dừng lại hoặc tiếp tục với ngày tiếp theo
                # continue
    else:
        print("Data is up-to-date. No new data to fetch.")


    # --- Generate DataFrames and Dump ---
    # Chỉ thực hiện nếu có dữ liệu mới được fetch hoặc dữ liệu ban đầu đã được load
    # Kiểm tra xem _data của lottery có dữ liệu không
    if lottery._data: # Giả định _data là nơi lưu trữ chính
        print("Generating DataFrames from collected data...")
        try:
            lottery.generate_dataframes()
            print("DataFrames generated.")
            print("Dumping updated data to files...")
            lottery.dump()
            print("Data dumped successfully.")
        except Exception as e:
            print(f"Error generating or dumping data: {e}")
    else:
        print("No data available (either loaded or fetched) to generate or dump.")

    print("Script finished.")

    # ------- PHẦN ANALYSIS ĐÃ BỊ XÓA TỪ ĐÂY TRỞ ĐI -------
