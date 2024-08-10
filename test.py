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

url = 'https://www.qimai.cn/app/rank/appid/475966832/country/cn'
# 发起GET请求
response = requests.get(url=url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    print("页面内容获取成功!")
    data=json.loads(response.text)
else:
    print(f"请求失败，状态码: {response.status_code}")
