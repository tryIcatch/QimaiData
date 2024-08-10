import re
import execjs
import requests


def get_cookie_value(cookie_string, name):
    regex = r"(^| )" + re.escape(name) + r"=([^;]*)(;|$)"
    match = re.search(regex, cookie_string)
    if match:
        return match.group(2)
    return None


def make_request(cookies,url,pm):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,en-GB-oxendict;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookies,
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

    # 从cookie中提取syncd和synct值
    syncd = -int(get_cookie_value(cookies, "syncd"))
    synct = int(get_cookie_value(cookies, "synct").replace('.', ''))


    params =pm.copy()
    params["syncd"]=syncd
    params["synct"]=synct


    with open('../js/qm.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    result = ctx.call('getAnalysis', url, params, cookies)

    print(result)
    params['analysis'] = result
    # print(param)
    del params["syncd"]
    del params["synct"]
    response = requests.get(url='https://api.qimai.cn{}'.format(url), params=params, headers=headers)
    return response.text
