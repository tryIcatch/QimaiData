import csv
import os

import requests
import json
# 设置请求头
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,en-GB-oxendict;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': 'syncd=-457; qm_check=A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWCwycRd1QlhAXFEGFUdeSklaHQdKAAkABAsgJ1dBWD0TR1JRRAp0BQlFEBQ3TSZKFUdBbwxvBBRFIlQsSUhTFxsQU1FVV1NHXEVYVElWBRsCHAkSSQ%3D%3D; PHPSESSID=ig2c9ikfnee9n4df5gjic7t51h; gr_user_id=4f739baa-fcb0-46b5-b5ef-5efc5dd1a1d9; ada35577182650f1_gr_session_id=ca0b3fc0-8b7a-46bb-a56b-d57d60ab4854; ada35577182650f1_gr_session_id_sent_vst=ca0b3fc0-8b7a-46bb-a56b-d57d60ab4854; USERINFO=LGqIlcVNtzEJyMViPnQppUtJiNKajHL%2BUUWgGiLlBltmQk9kbkia%2BL4Td4WXf1mCLR0zBPR22gFjPHFygB5EF3tlEbAhIlzaSJD6ytTMWh6IjO7KwGgwIrbTBMw8vB7TAgzuYrmb%2Fqygh9aKndYie3oH9VrPoDXz; AUTHKEY=SG59PdQWozBvUXS9sjPzP%2FiAXNA4tMVIqWnuf7EYQ89B5qug7BX3p57GqR3hq76DkMRC%2BPTMF4LmKImyXt%2Fl3%2FTdcVyKTFglZ5oHhsLKdiD2SC%2F%2FcVSbWQ%3D%3D; ada35577182650f1_gr_last_sent_sid_with_cs1=ca0b3fc0-8b7a-46bb-a56b-d57d60ab4854; ada35577182650f1_gr_last_sent_cs1=qm22311088822; ada35577182650f1_gr_cs1=qm22311088822; aso_ucenter=3742v9YN6pin2NxJ1ofncYhwzkwTPL7jD%2BnrvpaEdmdXi4VjbTRtDU5yYnfgVT0GteU; tgw_l7_route=29ef178f2e0a875a4327cbfe5fbcff7e;',
    'if-modified-since': 'Fri, 02 Aug 2024 02:22:18 GMT',
    'if-none-match': 'W/"66ac42da-c53"',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
}

# 目标URL
# url ='https://api.qimai.cn/rank/indexPlus/brand_id/2?analysis=dkZJFQkWElVcX1MGHDFVQxZJBRoZFx5qWFNMViEaAFReX1BPT0sEAwEjR1I%3D'
# url = 'https://api.qimai.cn/rank/indexPlus/brand_id/1?analysis=dkZJFQkWElVcX1MGHDFVQxZJBRoZFx5qWFNMVSEaAFReX1BPT0sEAwIjR1I%3D'
# url = 'https://api.qimai.cn/rank/indexPlus/brand_id/0?analysis=dkZJFQkWElVcX1MGHDFVQxZJBRoZFx5qWFNMVCEaAFReX1BPT0sEAwEjR1I%3D'
url = 'https://api.qimai.cn/rank/index?analysis=ex88DQoVIwNvZmETByZRQAcLMlU4WlVHUFkISwhXUgAeJ0tOSEINCAJUVlYOByVFVA%3D%3D&brand=free&country=cn&genre=36&device=iphone'

# 发起GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    print("页面内容获取成功!")
    data=json.loads(response.text)

    # 创建一个输出目录来保存 CSV 文件
    output_dir = "app_csv_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 定义 CSV 字段名
    csv_fields = [
        'App ID', 'Genre Sub ID', 'Index', 'App Name', 'Subtitle', 'Icon URL',
        'Publisher', 'Country', 'File Size', 'Price', 'Continuous First Days',
        'Last Release Time', 'Keyword Cover', 'Keyword Cover Top 3',
        'Company ID', 'Company Name', 'Rank A Ranking', 'Rank A Change', 'Rank A Genre',
        'Rank B Ranking', 'Rank B Change', 'Rank B Genre',
        'Rank C Ranking', 'Rank C Change', 'Rank C Genre',
        'Comment Rating', 'Comment Number', 'Is Ad'
    ]

    # 遍历每个应用并将其保存到单独的 CSV 文件中
    for app in data['rankInfo']:
        # 提取数据
        app_data = {
            'App ID': app.get('app_id', 'N/A'),
            'Genre Sub ID': app.get('genre_sub_id', 'N/A'),
            'Index': app.get('index', 'N/A'),
            'App Name': app['appInfo'].get('appName', 'N/A'),
            'Subtitle': app['appInfo'].get('subtitle', 'N/A'),
            'Icon URL': app['appInfo'].get('icon', 'N/A'),
            'Publisher': app['appInfo'].get('publisher', 'N/A'),
            'Country': app['appInfo'].get('country', 'N/A'),
            'File Size': app['appInfo'].get('file_size', 'N/A'),
            'Price': app['appInfo'].get('price', 'N/A'),
            'Continuous First Days': app['appInfo'].get('continuousFirstDays', 'N/A'),
            'Last Release Time': app.get('lastReleaseTime', 'N/A'),
            'Keyword Cover': app.get('keywordCover', 'N/A'),
            'Keyword Cover Top 3': app.get('keywordCoverTop3', 'N/A'),
            'Company ID': app['company'].get('id', 'N/A'),
            'Company Name': app['company'].get('name', 'N/A'),
            'Rank A Ranking': app['rank_a'].get('ranking', 'N/A'),
            'Rank A Change': app['rank_a'].get('change', 'N/A'),
            'Rank A Genre': app['rank_a'].get('genre', 'N/A'),
            'Rank B Ranking': app['rank_b'].get('ranking', 'N/A'),
            'Rank B Change': app['rank_b'].get('change', 'N/A'),
            'Rank B Genre': app['rank_b'].get('genre', 'N/A'),
            'Rank C Ranking': app['rank_c'].get('ranking', 'N/A'),
            'Rank C Change': app['rank_c'].get('change', 'N/A'),
            'Rank C Genre': app['rank_c'].get('genre', 'N/A'),
            'Comment Rating': app['comment'].get('rating', 'N/A'),
            'Comment Number': app['comment'].get('num', 'N/A'),
            'Is Ad': app.get('is_ad', 'N/A')
        }

        # 生成 CSV 文件名，使用 App ID 或其他唯一字段
        csv_filename = os.path.join(output_dir, f"{app_data['App Name']}.csv")

        # 写入 CSV 文件
        with open(csv_filename, 'w', newline='',  encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
            writer.writeheader()
            writer.writerow(app_data)

        print(f"数据已保存到: {csv_filename}")
else:
    print(f"请求失败，状态码: {response.status_code}")
