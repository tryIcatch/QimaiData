#更新日志：https://api.qimai.cn/app/compareVersion?analysis=ezE3VCcsHgJ7dW4UKQtwQyolUxE1EE4BfV0tDgNXfAkEID4QGkhjV1UOXVFjZ1hbJ0tXGApFHlQMCRFYRAAwAhoLEBVbcRRVVVkAB11VVFlMQDoWAg%3D%3D&appid=1479814602&country=cn&v1=2.8.2&v2=2.8.3&field=release_note
#下载量预估：https://api.qimai.cn/pred/download?analysis=ezE3VCcsHgJ7dW4UKQtwQSgMKhw1PR1BfHMEHSx9f1UqMylMNS50Am5RUFx5FUoWFQ0cVh5aRlkPCwBddkZQVlBBS0wEBQVUUiEaBQ%3D%3D&appid=1479814602&country=cn&sdate=2023-08-08&edate=2024-08-07
#收入预估：https://api.qimai.cn/pred/revenue?analysis=ezE3VCcsHgJ7dW4UKQtwQSgMKhw1PR1BfHMEHSx9f1UqMylMNS50Am5RUFx5FUoWFQ0cVghQR1INEQR5FVNXX1FKQEsNBwNTJEIK&appid=1479814602&country=cn&sdate=2023-08-08&edate=2024-08-07
#未删除评论： https://api.qimai.cn/app/commentNum?analysis=eyEjVyYCEk54ZWZRKSVwTygiLhI0LTsBfWMiUCxTdxwoJFgPNjkFRngkKhRgBFwSBT8uDB5zCEIHM1EEdkZJBhgIVhlaXFoGChV3QwgmRF5JQUMGAQNTXFULdkZV&export_type=comment_num&appid=1479814602&country=cn&delete=0&sdate=2023-08-08&edate=2024-08-08
#已删除评论：https://api.qimai.cn/app/commentNum?analysis=ezEjVyYCEk54ZWZRKSVwTygiLhI0LTsBfWMiUCxTdxwoJFgPNjkFRngkKhRgBFwSBT8uDB5zCEIHM1EEdkZJBhgIVhlaXFoGChV3QwgmRF5JQUMGAQBaVlMKdkZV&export_type=comment_num&appid=1479814602&country=cn&delete=1&sdate=2023-08-08&edate=2024-08-08
#总榜排名：https://api.qimai.cn/app/rankMore?analysis=ezEjHyUsPEp7S1xXKTVoBCgiLhE1PTNPfWMiUC1td1ErDSkBNzkFRnggVBZ2cSMVBS8%2BDhlzCE46M1RLb1dTCgsVLxZ1EhgCFBEWRAQIDCUXCx91EgFSXFgKB1dQXltLOVkG&appid=1479814602&country=cn&export_type=app_rank&brand=free&day=1&appRankShow=1&subclass=all&simple=1&sdate=2023-08-08&edate=2024-08-08&rankEchartType=1
#状态信息：https://api.qimai.cn/app/appStatusList?analysis=dkYHFxhXGApFYkMCEBRKegwVEyhbT0sNCARbVFMJBVEmRFs%3D
#评分：https://api.qimai.cn/app/commentRateNum?analysis=ezE3VCcsHgJ7dW4UKQtwQSgMKhw1PR1BfHMEHSx9f1UqMylMNS50BW5RUQtbBFQSPT9NSSIGe18HIzdfVAswEzI%2FP091EhgCFBEWVQoLCg0WDShURVItEQx5FVNXX1FLQEINAA9XJEIK&export_type=comment_rate_num&appid=1479814602&country=cn&sdate=2023-08-08&edate=2024-08-08&typec=day
import json
import os

import pandas as pd
import requests
from RequestQM.request_interface import make_request
from js_encoder.get_analysis import get_analysis

import  csv
import  time
# 加载CSV文件
file_path = 'selected_app_info.csv'
app_info_df = pd.read_csv(file_path)
cookies="qm_check=A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWCwycRd1QlhAXFEGFUdeSklaHQdKAAkABAsgJ1dBWD0TR1JRRAp0BQlFEBQ3TSZKFUdBbwxvBBRFIlQsSUhTFxsQU1FVV1NHXEVYVElWBRsCHAkSSQ%3D%3D; PHPSESSID=ig2c9ikfnee9n4df5gjic7t51h; gr_user_id=4f739baa-fcb0-46b5-b5ef-5efc5dd1a1d9; USERINFO=LGqIlcVNtzEJyMViPnQppUtJiNKajHL%2BUUWgGiLlBltmQk9kbkia%2BL4Td4WXf1mCLR0zBPR22gFjPHFygB5EF3tlEbAhIlzaSJD6ytTMWh6IjO7KwGgwIrbTBMw8vB7TAgzuYrmb%2Fqygh9aKndYie3oH9VrPoDXz; AUTHKEY=SG59PdQWozBvUXS9sjPzP%2FiAXNA4tMVIqWnuf7EYQ89B5qug7BX3p57GqR3hq76DkMRC%2BPTMF4LmKImyXt%2Fl3%2FTdcVyKTFglZ5oHhsLKdiD2SC%2F%2FcVSbWQ%3D%3D; ada35577182650f1_gr_last_sent_cs1=qm22311088822; aso_ucenter=3742v9YN6pin2NxJ1ofncYhwzkwTPL7jD%2BnrvpaEdmdXi4VjbTRtDU5yYnfgVT0GteU; ada35577182650f1_gr_cs1=qm22311088822; synct=1723255958.692; syncd=96; tgw_l7_route=29ef178f2e0a875a4327cbfe5fbcff7e"
params = {
    'country': 'cn',
"sdate": "2023-08-09",
"edate": "2024-08-09",

}
url= "/pred/download"

folder_path = "免费应用下载量数据"  # 你可以更改为想要保存文件的文件夹路径
# 如果文件夹不存在，则创建它
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
for appid,appName in zip(app_info_df['app_id'],app_info_df['appInfo.appName']):
    params["appid"] = appid

    print(appid,appName)

    # 准备写入 CSV 文件
    filename = os.path.join(folder_path, f"{appName}.csv")


    if os.path.exists(filename):
        print(f" {filename} 存在，跳过......")
        continue

    # 发送请求并解析响应
    response = json.loads(make_request(cookies=cookies, url=url, pm=params))
    lgth = len(response["data"]["list"])



    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # 写入 CSV 文件的表头
        writer.writerow(
            ["appid","appName", "avgList_date", "avgList_value", "list_date", "list_value", "versionDate", "version", "date"])
        versionDict = response["data"]["version"]

        # 循环处理数据
        for i in range(lgth):
            avgList_date = response["data"]["avgList"][i][0]
            avgList_value = response["data"]["avgList"][i][1]
            List_date = response["data"]["list"][i][0]
            List_value = response["data"]["list"][i][1]


            # 默认情况下将 versionDate, version 和 date 设置为空
            versionDate, version, date = "", "", ""

            # 如果 i 在 versionDict 中，则获取相应的值
            if i in versionDict.keys():
                versionDate = versionDict[i]["versionDate"]
                version = versionDict[i]["version"]
                date = versionDict[i]["date"]


            # 写入一行数据到 CSV 文件
            writer.writerow([appid, appName,avgList_date, avgList_value, List_date, List_value, versionDate, version, date])

    print(f"File {appName} saved.")

    # 在循环结束后等待5秒钟
    time.sleep(5)


