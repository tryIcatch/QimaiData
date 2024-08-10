import base64
import time
import datetime

import execjs

def get_analysis(url, params):
    jscode = '''
    function o() {
        return unescape("861831832863830866861836861862839831831839862863839830865834861863837837830830837839836861835833".replace(/8/g, "%u00"))
    }
    function i() {
        var e = "";
        return ["66", "72", "6f", "6d", "43", "68", "61", "72", "43", "6f", "64", "65"].forEach(function(t) {
            e += unescape("%u00" + t)
        }),
            e
    }
    function r(e) {
        var t = i();
        return String[t](e)
    }

    function f(e, t) {
        t || (t = o()),
        e = e.split("");
        var array=new Array(e.length)

        for (var n = e.length, a = t.length, i = "charCodeAt", s = 0; s < n; s++)
            array  ^ t )
        return array.join("");
    }

    function get_data(s1){
        s2 = '0000000c735d856'
        return f(s1,s2)
    }
    '''

    js = execjs.compile(jscode)

    today = str(datetime.datetime.today()).split()[0]

    r = ''.join(sorted(params))
    base64_r = base64.b64encode(r.encode('utf-8')).decode('utf-8')

    base_url = 'https://api.qimai.cn'
    timestamp = int(time.time() * 1000 - 1661224081041)
    _ = '@#'

    str_r = base64_r + _ + url + _ + str(timestamp) + _ + '1'
    str_r = str_r.replace(base_url, '')

    an = js.call('get_data', str_r)
    analysis = base64.b64encode(an.encode('utf-8')).decode('utf-8')

    return analysis