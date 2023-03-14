!function(e) {
    function n(data) {
        for (var n, t, d = data[0], l = data[1], f = data[2], i = 0, m = []; i < d.length; i++)
            t = d[i],
            Object.prototype.hasOwnProperty.call(o, t) && o[t] && m.push(o[t][0]),
            o[t] = 0;
        for (n in l)
            Object.prototype.hasOwnProperty.call(l, n) && (e[n] = l[n]);
        for (h && h(data); m.length; )
            m.shift()();
        return c.push.apply(c, f || []),
        r()
    }
    function r() {
        for (var e, i = 0; i < c.length; i++) {
            for (var n = c[i], r = !0, t = 1; t < n.length; t++) {
                var l = n[t];
                0 !== o[l] && (r = !1)
            }
            r && (c.splice(i--, 1),
            e = d(d.s = n[0]))
        }
        return e
    }
    var t = {}
      , o = {
        32: 0
    }
      , c = [];
    function d(n) {
        if (t[n])
            return t[n].exports;
        var r = t[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return e[n].call(r.exports, r, r.exports, d),
        r.l = !0,
        r.exports
    }
    d.e = function(e) {
        var n = []
          , r = o[e];
        if (0 !== r)
            if (r)
                n.push(r[2]);
            else {
                var t = new Promise((function(n, t) {
                    r = o[e] = [n, t]
                }
                ));
                n.push(r[2] = t);
                var c, script = document.createElement("script");
                script.charset = "utf-8",
                script.timeout = 120,
                d.nc && script.setAttribute("nonce", d.nc),
                script.src = function(e) {
                    return d.p + "" + ({
                        0: "commons/5b7f9e1d",
                        1: "vendors/f2d66b02",
                        2: "vendors/0f68e262",
                        5: "pages/album_detail/_index",
                        6: "pages/blackshark/index",
                        7: "pages/callback",
                        8: "pages/down/index",
                        9: "pages/downtingshu/index",
                        10: "pages/index",
                        11: "pages/logout/index",
                        12: "pages/musician/index",
                        13: "pages/musician/page",
                        14: "pages/mvplay/_index",
                        15: "pages/mvs/index",
                        16: "pages/play_detail/_index",
                        17: "pages/playlist_detail/_index",
                        18: "pages/playlists/index",
                        19: "pages/rankList/index",
                        20: "pages/search",
                        21: "pages/search/album",
                        22: "pages/search/list",
                        23: "pages/search/mv",
                        24: "pages/search/playlist",
                        25: "pages/search/singers",
                        26: "pages/singer_detail/_index",
                        27: "pages/singer_detail/index/album",
                        28: "pages/singer_detail/index/index",
                        29: "pages/singer_detail/index/info",
                        30: "pages/singer_detail/index/mv",
                        31: "pages/singers/index"
                    }[e] || e) + "." + {
                        0: "49eb33f",
                        1: "587cb3e",
                        2: "4deec49",
                        5: "214d36c",
                        6: "c52f389",
                        7: "ffdfc35",
                        8: "69d3da0",
                        9: "6d1403d",
                        10: "f0518a6",
                        11: "f143a16",
                        12: "5d57ec4",
                        13: "2613fa6",
                        14: "b36e3d9",
                        15: "be8aee6",
                        16: "2364cdc",
                        17: "1e333a0",
                        18: "8adeb3e",
                        19: "576719e",
                        20: "1590f44",
                        21: "04161fa",
                        22: "4ecc2eb",
                        23: "9bbf59f",
                        24: "4386338",
                        25: "a55a1fa",
                        26: "126d485",
                        27: "4c56e09",
                        28: "79233c4",
                        29: "33c7c29",
                        30: "c636a40",
                        31: "a8f02e8"
                    }[e] + ".js"
                }(e);
                var l = new Error;
                c = function(n) {
                    script.onerror = script.onload = null,
                    clearTimeout(f);
                    var r = o[e];
                    if (0 !== r) {
                        if (r) {
                            var t = n && ("load" === n.type ? "missing" : n.type)
                              , c = n && n.target && n.target.src;
                            l.message = "Loading chunk " + e + " failed.\n(" + t + ": " + c + ")",
                            l.name = "ChunkLoadError",
                            l.type = t,
                            l.request = c,
                            r[1](l)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var f = setTimeout((function() {
                    c({
                        type: "timeout",
                        target: script
                    })
                }
                ), 12e4);
                script.onerror = script.onload = c,
                document.head.appendChild(script)
            }
        return Promise.all(n)
    }
    ,
    d.m = e,
    d.c = t,
    d.d = function(e, n, r) {
        d.o(e, n) || Object.defineProperty(e, n, {
            enumerable: !0,
            get: r
        })
    }
    ,
    d.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    d.t = function(e, n) {
        if (1 & n && (e = d(e)),
        8 & n)
            return e;
        if (4 & n && "object" == typeof e && e && e.__esModule)
            return e;
        var r = Object.create(null);
        if (d.r(r),
        Object.defineProperty(r, "default", {
            enumerable: !0,
            value: e
        }),
        2 & n && "string" != typeof e)
            for (var t in e)
                d.d(r, t, function(n) {
                    return e[n]
                }
                .bind(null, t));
        return r
    }
    ,
    d.n = function(e) {
        var n = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return d.d(n, "a", n),
        n
    }
    ,
    d.o = function(object, e) {
        return Object.prototype.hasOwnProperty.call(object, e)
    }
    ,
    d.p = "https://h5static.kuwo.cn/www/kw-www/",
    d.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    var l = window.webpackJsonp = window.webpackJsonp || []
      , f = l.push.bind(l);
    l.push = n,
    l = l.slice();
    for (var i = 0; i < l.length; i++)
        n(l[i]);
    var h = f;
    r()
}([]);
