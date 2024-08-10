import json

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
url = 'https://api.qimai.cn/rank/index?analysis=ex88DQoVIwNvZmETByZRQAcLMlU4WlVHUFkISwhXUgAeJ0tOSEINCAJUVlYOByVFVA%3D%3D&brand=free&country=cn&genre=36&device=iphone'
response = requests.get(url=url,headers=headers)
json_data = json.loads(response.text)
# print(json_data)
# print(type(json_data))
# Step 2: 提取所有字段
# 初始化一个空的集合，用来存储所有字段名
all_fields = set()

# 遍历JSON数据，获取所有字段
for item in json_data:
    all_fields.update(item.keys())

# Step 3: 提取数据
# 创建一个字典来存储所有字段的数据
extracted_data = {field: [] for field in all_fields}

# 遍历JSON数据并填充字段数据
for item in json_data:
    for field in all_fields:
        extracted_data[field].append(item.get(field, None))

# Step 4: 将提取的数据转换为DataFrame
df = pd.DataFrame(extracted_data)

# Step 5: 将数据保存到CSV文件中
output_file = 'output_data.csv'
df.to_csv(output_file, index=False)

print(f"数据已保存到 {output_file}")
