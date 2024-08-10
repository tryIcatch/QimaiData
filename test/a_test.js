var i = {
    sf: function sf(n,t) {
  n = new RegExp("(^| )" + n + "=([^;]*)(;|$)");
  return (n = t["cookie"].match(n)) ? unescape(n[2]) : null;
  },

    cv: function v(t) {
        t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function(n, t) {
            return o('0x' + t);
        });

        try {
            return btoa(t);
        } catch (n) {
            return Buffer["from"](t)["toString"]('base64');
        }
    },

    oZ: function h(n, t) {
        t = t || u();
        for(var e = (n=n["split"](""))["length"],r=t["length"],a="charCodeAt", i = 0;i<e; i++) {
            n[i]=o(n[i][a](0)^t[(i+10)%r][a](0));
            return n["join"]("")
        }
    },
    ej: function ej(t) {
    // var regex = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    // var matches = t["cookie"].match(regex);
    var matches = t["params"]["syncd"]
    return matches ? decodeURIComponent(matches[2]) : null;
},
   vf: function vf(t) {
  t = encodeURIComponent(t).replace(/%([0-9A-F]{2})/g, function (n, t) {
    return ofn("0x" + t);
  });
  try {
    return btoa(t);
  } catch (n) {
    return Buffer.from(t).toString("base64");
  }
},
   hf: function hf(n, t) {
  // t = t || u();
  for (
    let e = (n = n.split("")).length, r = t.length, a = "charCodeAt", i = 0;
    i < e;
    i++
  ) {
    n[i] = ofn(n[i][a](0) ^ t[(i + 10) % r][a](0));
  }
  return n.join("");
}


};
            function u() {
                return unescape("861831832863830866861836861862839831831839862863839830865834861863837837830830837839836861835833"["replace"](/8/g, "%u00"))
            }
// function o(n) {
//                 t = "",
//                 ["66", "72", "6f", "6d", "43", "68", "61", "72", "43", "6f", "64", "65"]["forEach"](function(n) {
//                     t += unescape("%u00" + n)
//                 });
//                 var t, e = t;
//                 return String[e](n)

function o(n) {
                return String["fromCharCode"](n)
}
function ofn(n) {
  (t = ""),
    [
      "66",
      "72",
      "6f",
      "6d",
      "43",
      "68",
      "61",
      "72",
      "43",
      "6f",
      "64",
      "65",
    ].forEach(function (n) {
      t += unescape("%u00" + n);
    });
  var t,
    e = t;
  return String[e](n);
}
function fn(t) {
    var e;
    // var syncd = i.ej(t);
    // var currentTime = +new Date();
    var startTime = t["params"]["synct"];
    // var s =  -(0, i["ej"])(t) || +new Date() - startTime;


    // var s =  t["params"]["syncd"];
    // s=281
    // startTime=1723189375964
    // Calculate `s`
    // var s = -(syncd ? parseInt(syncd, 10) : currentTime - startTime);

    // Calculate `r`

    delete  t.params.syncd
    delete  t.params.synct
    var a = [];
    var v = "@#";
    var d = "xyz517cda96efgh";
    var n = String(startTime/1000)
    var s =  -(0, i["sf"])(n,t) || +new Date() - startTime;
    var  r = +new Date() - (s || 0) - 1661224081041;
    Object["keys"](t["params"])["forEach"](function(n) {
        if (n === 'analysis')
            return !1;
        t["params"]["hasOwnProperty"](n) && a["push"](t["params"][n]);
    });
    // a = a.slice(0,2)

    a = a.sort().join("");
    a = i.vf(a);
    a = (a += v + t.url.replace(t.baseURL, "")) + (v + r) + (v + 3);
    // NjQ0NDE3MDk2NWNu@#/app/appinfo@#61958299938@#3"
    // NjQ0NDE3MDk2NWNu@#/app/appinfo?@#61968384649@#3
    e = i.vf(i.hf(a, d));

    // if (t.url.indexOf("analysis") == -1) {
    //     t.url += (t.url.indexOf("?") != -1 ? "&" : "?") + "analysis=" + encodeURIComponent(e);
    // }
// "NjQ0NDE3MDk2NWNu@#/app/appinfo@#61958299938@#3"
    return e;
}
function getAnalysis(url, pm,cookies) {
    var params = {
        "url": url,
        "baseURL": "https://api.qimai.cn",
        "params": pm,
        "cookie":cookies
    };
    return fn(params);
}