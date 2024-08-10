import json
import os

import requests
import pandas as pd
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

# Step 1: 获取JSON数据（假设从某个API接口获取）
# url = 'https://api.qimai.cn/rank/index?analysis=ex88DQoVIwNvZmETByZRQAcLMlU4WlVHUFkISwhXUgAeJ0tOSEINCAJUVlYOByVFVA%3D%3D&brand=free&country=cn&genre=36&device=iphone'
# url = 'https://api.qimai.cn/rank/index?analysis=ezEjUycSMEp6W3ZTKQtwQSgMNhw1PR1BfHMEHi9UeBA8CSIUIy1ZRlYkXRRjZ1hbJ0tXCxtbWhgKCgVcTiVFUVlAQUMDBQNUVVZ5FVY%3D&brand=free&country=cn&genre=36&device=iphone&date=2024-08-08&page=2&is_rank_index=1&snapshot=18:24:04'
# url = 'https://api.qimai.cn/rank/index?analysis=ezEjUycSMEp6W3ZTKQt4TyslVx83OkpCfnMuHi9UeBA8CSIUIy1ZRlYkXRRjZ1hbJ0tXCxtbWhgKCgVcTiVFUVlAQE8DAAdVV1V5FVY%3D&brand=free&country=cn&genre=36&device=iphone&date=2024-08-08&page=3&is_rank_index=1&snapshot=18:24:04'
url = 'https://api.qimai.cn/rank/index?analysis=ezEjUycSMEp6W3ZTKQt4TyslVx83OkpCfnMuVi9%2BeBA8CSIUIy1ZRlYkXRRjZ1hbJ0tXCxtbWhgKCgVcTiVFUVlAQE8CBQBWXFJ5FVY%3D&brand=free&country=cn&genre=36&device=iphone&date=2024-08-08&page=4&is_rank_index=1&snapshot=18:24:04'
response = requests.get(url=url,headers=headers)
# Step 2: 提取rankInfo数据
json_data=json.loads(response.text)
rank_info_list = json_data.get('rankInfo', [])

# 如果rankInfo为空或不是列表，打印警告并退出
if not isinstance(rank_info_list, list):
    print("rankInfo不是一个列表或为空")
    exit()

# Step 3: 解析rankInfo中的字段
data = []

for item in rank_info_list:
    record = {}
    if isinstance(item, dict):
        # 提取顶层字段
        for key, value in item.items():
            if isinstance(value, dict):
                # 如果值是字典，提取字典中的字段
                for sub_key, sub_value in value.items():
                    record[f"{key}.{sub_key}"] = sub_value
            elif isinstance(value, list):
                # 如果值是列表，处理列表中的字典
                for sub_item in value:
                    if isinstance(sub_item, dict):
                        for sub_key, sub_value in sub_item.items():
                            record[f"{key}.{sub_key}"] = sub_value
            else:
                record[key] = value
    data.append(record)

# Step 4: 将数据转换为DataFrame
df = pd.DataFrame(data)

# Step 5: 将数据保存到CSV文件中
output_file = 'rank_info_data.csv'
if os.path.exists(output_file):
    df.to_csv(output_file, mode='a', header=False, index=False)
else:
    df.to_csv(output_file, mode='w', header=True, index=False)

print(f"数据已追加到 {output_file}")