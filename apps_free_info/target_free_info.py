import os

import pandas as pd
import requests

# Load the CSV file
file_path = 'rank_info_data.csv'
rank_info_data = pd.read_csv(file_path)

# 选择所需的列

selected_columns = rank_info_data[['app_id', 'appInfo.appName', 'appInfo.publisher', 'appInfo.price']]


# 将价格为0的替换为“免费”
selected_columns['appInfo.price'] = selected_columns['appInfo.price'].apply(lambda x: '免费' if x == 0 else x)

# Display the selected columns

# Define the output file path
output_file_path = 'selected_app_info.csv'

# Check if the output file exists
if not os.path.exists(output_file_path):
    # Save the selected columns to a new CSV file
    selected_columns.to_csv(output_file_path, index=False)
    print(f'File created: {output_file_path}')
else:
    print(f'File already exists: {output_file_path}')
