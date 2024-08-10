import re
import time
from urllib.parse import quote


class DecodeEncry:
    """
    七麦数据参数加密函数
    get_s,j,d三个主要加密
    """
    c_params = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "+", "/"]

    def j(self, n):
        a = quote(n)
        l = re.findall("%([0-9A-F]{2})", a)
        for i in l:
            a = a.replace("%" + i, chr(int("0x" + i, 16)))
        return self.nfun(a)

    def nfun(self, e):
        n = self.efun(e, "binary")
        return self.qfun("base64", n)

    def efun(self, e, t):
        return self.d_j(None, e, t)

    def a(self, e, t):
        e = t * [0]
        return e

    def d_j(self, e, t, n):
        i = len(t)
        e = self.a(e, i)
        r = self.e_write(t, n, e)
        e = e[0:r]
        return e

    def e_write(self, e, t, this1):
        i = t
        t = 0
        n = len(this1)
        r = len(this1) - t
        return self.L(this1, e, t, n)

    def L(self, e, t, n, i):
        return self.S1(e, t, n, i)

    def S1(self, e, t, n, i):
        return self.q1(self.G1(t), e, n, i)

    def G1(self, e2):
        t = []
        for n in range(len(e2)):
            t.append(255 & ord(e2[n]))
        return t

    def q1(self, e, t, n, i):
        r = 0
        while 1:
            if r < i and (not ((r + n) >= len(t) or r >= len(e))):
                t[r + n] = e[r]
                r += 1
            else:
                break
        return r

    def qfun(self, t, this1):
        e = len(this1)
        return self.y(this1, t)

    def y(self, this1, e):
        n = len(this1)
        return self.D(this1, 0, n)

    def D(self, e, t, n):
        return self.u1(e[t:n])

    def u1(self, e):
        n = len(e)
        r = []
        a = 16383
        o = 0
        while 1:
            i = n % 3
            s = n - i
            if o < s:
                r.append(self.l_u(e, o, s if (o + a) > s else o + a))
                o += a
            else:
                break
        if 1 == i:
            t = e[n - 1]
            r.append(self.c_params[t >> 2] + self.c_params[t << 4 & 63] + "==")
        else:
            t = (e[n - 2] << 8) + e[n - 1]
            r.append(self.c_params[t >> 10] + self.c_params[t >> 4 & 63] + self.c_params[t << 2 & 63] + "=")
        return "".join(r)

    def l_u(self, e, t, n):
        r = []
        a = t
        while 1:
            if a < n:
                i = (e[a] << 16 & 16711680) + (e[a + 1] << 8 & 65280) + (255 & e[a + 2])
                r.append(self.s3(i))
            else:
                break
            a += 3
        return "".join(r)

    def s3(self, e):
        return self.c_params[e >> 18 & 63] + self.c_params[e >> 12 & 63] + self.c_params[e >> 6 & 63] + self.c_params[
            63 & e]

    def d(self, e, t):
        # d加密函数
        if not t:
            t = "a12c0fa6ab9119bc90e4ac7700796a53"
        e1 = list(e)
        n = len(t)
        a = len(e1)
        for s1 in range(a):
            e1[s1] = chr((ord(e1[s1][0]) ^ ord(t[(s1 + 10) % n][0])))
        return "".join(e1)

    def get_s(self, P, syncd, synct, url, params):
        # 获取s加密参数
        A = -syncd or int(time.time() * 1000) - 1000 * synct
        r = str(int(time.time() * 1000) - A - 1661224081041)
        z = "@#"
        s = "".join(sorted([str(v) for v in params.values()]))
        s = self.j(s)
        s += z + url
        s += z + r
        s += z + "1"
        return s


    def get_analysis(self, synct, url, params):
        P = "00000008d78d46a"
        ut = int(time.time() * 1000)
        syncd = int(1000 * float(synct)) - ut
        d = DecodeEncry()
        e1_ = d.get_s(P, syncd, synct, url.replace("https://api.qimai.cn", ""), params)
        n = d.d(e1_, P)
        analysis = d.j(n)
        return analysis