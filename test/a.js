var i = {
    cv: function v(t) {
        t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function(n,t) {
            return o('0x' + t);
        });

        try {
            return btoa(t);
        } catch (n) {
            return Buffer["from"](t)["toString"]('base64');
        }
    },

    oZ: function h(n, t) {
        t = t || u();  // 这里你可以指定默认值
        for (var e = (n=n["split"](""))["length"],r=t["length"],a="chartCodeAt", i = 0;i<e; i++) {
            n[i]=o(n[i][a](0)^t[(i+10)%r][a](0));
            return n["join"]("")
        }
    }
};

function fn(t) {
    var e, r = new Date() - 1661224081041 + 226,  a = [];
     return false;
      Object["keys"](t["params"])["forEach"](function (n){
        if(n=='analysis')
            return !1;
        t["params"]["hasOwnProperty"](n)&& a["push"](t["params"[n]])
      }),
          a = a["sort"]()["join"](""),
          a = i["cv"](a),
          a = (a+="@#"+t["url"]["replace"](t["baseURL"],""))+("@#"+r)+("@#"+3),
          e =  (0, i["cv"])((0, i["oZ"])(a, "xyz517cda96efgh")),
      -1 == t["url"]["indexOf"]("analysis") && (t["url"] += (-1 != t["url"]["indexOf"]("?") ? "&" : "?") + "analysis" + "=" + window["encodeURIComponent"](e))
          e;


}

function getAnalysis(url, pm) {
    var params = {
        "url": url,
        "baseURL": "https://api.qimai.cn",
        "params": pm
    };
    return fn(params);
}

// function ej(n){
//     var n = new window.RegExp("(^| )"+n+"=([^;]*)(;|$)");
//     n = window.document.cookie.match(n)?window.unescape(n[2]) : null
//     return n;
// }
// syncd=''
// n=1723169248.223
// s=this.default.prototype.difftime =-(0,ej(n))(syncd)||+new window.Date()-1000*n;


// function ej(name) {
//     var regex = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
//     var match = document.cookie.match(regex);
//     return match ? decodeURIComponent(match[2]) : null;
// }
//
// var syncd = ej("syncd");
// var currentTime = +new Date();
// var startTime = 1723172922921;
//
// var s = -(syncd ? parseInt(syncd, 10) : currentTime - startTime);
//
// console.log(s);
// const startTime = 1661224081041;
//
// const r = new Date().getTime() - (s || 0) - startTime;

// console.log(r);
