function c_a(e, t) {
            var n = "undefined" !== typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
            if (!n) {
                if (Array.isArray(e) || (n = i(e)) || t && e && "number" === typeof e.length) {
                    n && (e = n);
                    var r = 0
                      , a = function() {};
                    return {
                        s: a,
                        n: function() {
                            return r >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[r++]
                            }
                        },
                        e: function(e) {
                            throw e
                        },
                        f: a
                    }
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }
            var o, s = !0, c = !1;
            return {
                s: function() {
                    n = n.call(e)
                },
                n: function() {
                    var e = n.next();
                    return s = e.done,
                    e
                },
                e: function(e) {
                    c = !0,
                    o = e
                },
                f: function() {
                    try {
                        s || null == n["return"] || n["return"]()
                    } finally {
                        if (c)
                            throw o
                    }
                }
            }
        }

function t_wordsToBytes(e) {
                    for (var t = [], n = 0; n < 32 * e.length; n += 8)
                        t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
                    return t
                }

var n_word = {
            utf8: {
                stringToBytes: function(e) {
                    return n_word.bin.stringToBytes(unescape(encodeURIComponent(e)))
                },
                bytesToString: function(e) {
                    return decodeURIComponent(escape(n_word.bin.bytesToString(e)))
                }
            },
            bin: {
                stringToBytes: function(e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push(255 & e.charCodeAt(n));
                    return t
                },
                bytesToString: function(e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push(String.fromCharCode(e[n]));
                    return t.join("")
                }
            }
        }

function t_bytesToWords(e) {
                    for (var t = [], n = 0, r = 0; n < e.length; n++,
                    r += 8)
                        t[r >>> 5] |= e[n] << 24 - r % 32;
                    return t
                }

function o_ff(e, t, n, r, i, a, o) {
                var s = e + (t & n | ~t & r) + (i >>> 0) + o;
                return (s << a | s >>> 32 - a) + t
            }

o_gg = function(e, t, n, r, i, a, o) {
                var s = e + (t & r | n & ~r) + (i >>> 0) + o;
                return (s << a | s >>> 32 - a) + t
            }
,
o_hh = function(e, t, n, r, i, a, o) {
        var s = e + (t ^ n ^ r) + (i >>> 0) + o;
        return (s << a | s >>> 32 - a) + t
    }
,
o_ii = function(e, t, n, r, i, a, o) {
        var s = e + (n ^ (t | ~r)) + (i >>> 0) + o;
        return (s << a | s >>> 32 - a) + t
    }
          function n_rotl(e, t) {
            return e << t | e >>> 32 - t
        }

function t_endian(e) {
                    if (e.constructor == Number)
                        return 16711935 & n_rotl(e, 8) | 4278255360 & n_rotl(e, 24);
                    for (var t = 0; t < e.length; t++)
                        e[t] = t_endian(e[t]);
                    return e
                }

function o(e, n) {
    e.constructor == String ? e = n && "binary" === n.encoding ? a.stringToBytes(e) : n_word.utf8.stringToBytes(e) : i(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
    for (var s = t_bytesToWords(e), c = 8 * e.length, u = 1732584193, l = -271733879, h = -1732584194, d = 271733878, f = 0; f < s.length; f++)
        s[f] = 16711935 & (s[f] << 8 | s[f] >>> 24) | 4278255360 & (s[f] << 24 | s[f] >>> 8);
    s[c >>> 5] |= 128 << c % 32,
    s[14 + (c + 64 >>> 9 << 4)] = c;
    var p = o_ff
      , m = o_gg
      , v = o_hh
      , g = o_ii;
    for (f = 0; f < s.length; f += 16) {
        var b = u
          , y = l
          , w = h
          , _ = d;
        u = p(u, l, h, d, s[f + 0], 7, -680876936),
        d = p(d, u, l, h, s[f + 1], 12, -389564586),
        h = p(h, d, u, l, s[f + 2], 17, 606105819),
        l = p(l, h, d, u, s[f + 3], 22, -1044525330),
        u = p(u, l, h, d, s[f + 4], 7, -176418897),
        d = p(d, u, l, h, s[f + 5], 12, 1200080426),
        h = p(h, d, u, l, s[f + 6], 17, -1473231341),
        l = p(l, h, d, u, s[f + 7], 22, -45705983),
        u = p(u, l, h, d, s[f + 8], 7, 1770035416),
        d = p(d, u, l, h, s[f + 9], 12, -1958414417),
        h = p(h, d, u, l, s[f + 10], 17, -42063),
        l = p(l, h, d, u, s[f + 11], 22, -1990404162),
        u = p(u, l, h, d, s[f + 12], 7, 1804603682),
        d = p(d, u, l, h, s[f + 13], 12, -40341101),
        h = p(h, d, u, l, s[f + 14], 17, -1502002290),
        l = p(l, h, d, u, s[f + 15], 22, 1236535329),
        u = m(u, l, h, d, s[f + 1], 5, -165796510),
        d = m(d, u, l, h, s[f + 6], 9, -1069501632),
        h = m(h, d, u, l, s[f + 11], 14, 643717713),
        l = m(l, h, d, u, s[f + 0], 20, -373897302),
        u = m(u, l, h, d, s[f + 5], 5, -701558691),
        d = m(d, u, l, h, s[f + 10], 9, 38016083),
        h = m(h, d, u, l, s[f + 15], 14, -660478335),
        l = m(l, h, d, u, s[f + 4], 20, -405537848),
        u = m(u, l, h, d, s[f + 9], 5, 568446438),
        d = m(d, u, l, h, s[f + 14], 9, -1019803690),
        h = m(h, d, u, l, s[f + 3], 14, -187363961),
        l = m(l, h, d, u, s[f + 8], 20, 1163531501),
        u = m(u, l, h, d, s[f + 13], 5, -1444681467),
        d = m(d, u, l, h, s[f + 2], 9, -51403784),
        h = m(h, d, u, l, s[f + 7], 14, 1735328473),
        l = m(l, h, d, u, s[f + 12], 20, -1926607734),
        u = v(u, l, h, d, s[f + 5], 4, -378558),
        d = v(d, u, l, h, s[f + 8], 11, -2022574463),
        h = v(h, d, u, l, s[f + 11], 16, 1839030562),
        l = v(l, h, d, u, s[f + 14], 23, -35309556),
        u = v(u, l, h, d, s[f + 1], 4, -1530992060),
        d = v(d, u, l, h, s[f + 4], 11, 1272893353),
        h = v(h, d, u, l, s[f + 7], 16, -155497632),
        l = v(l, h, d, u, s[f + 10], 23, -1094730640),
        u = v(u, l, h, d, s[f + 13], 4, 681279174),
        d = v(d, u, l, h, s[f + 0], 11, -358537222),
        h = v(h, d, u, l, s[f + 3], 16, -722521979),
        l = v(l, h, d, u, s[f + 6], 23, 76029189),
        u = v(u, l, h, d, s[f + 9], 4, -640364487),
        d = v(d, u, l, h, s[f + 12], 11, -421815835),
        h = v(h, d, u, l, s[f + 15], 16, 530742520),
        l = v(l, h, d, u, s[f + 2], 23, -995338651),
        u = g(u, l, h, d, s[f + 0], 6, -198630844),
        d = g(d, u, l, h, s[f + 7], 10, 1126891415),
        h = g(h, d, u, l, s[f + 14], 15, -1416354905),
        l = g(l, h, d, u, s[f + 5], 21, -57434055),
        u = g(u, l, h, d, s[f + 12], 6, 1700485571),
        d = g(d, u, l, h, s[f + 3], 10, -1894986606),
        h = g(h, d, u, l, s[f + 10], 15, -1051523),
        l = g(l, h, d, u, s[f + 1], 21, -2054922799),
        u = g(u, l, h, d, s[f + 8], 6, 1873313359),
        d = g(d, u, l, h, s[f + 15], 10, -30611744),
        h = g(h, d, u, l, s[f + 6], 15, -1560198380),
        l = g(l, h, d, u, s[f + 13], 21, 1309151649),
        u = g(u, l, h, d, s[f + 4], 6, -145523070),
        d = g(d, u, l, h, s[f + 11], 10, -1120210379),
        h = g(h, d, u, l, s[f + 2], 15, 718787259),
        l = g(l, h, d, u, s[f + 9], 21, -343485551),
        u = u + b >>> 0,
        l = l + y >>> 0,
        h = h + w >>> 0,
        d = d + _ >>> 0
    }
    return t_endian([u, l, h, d])
};

function l(e, n) {
                if (void 0 === e || null === e)
                    throw new Error("Illegal argument " + e);
                var r = t_wordsToBytes(o(e, n));
                return n && n.asBytes ? r : n && n.asString ? n_word.bin.bytesToString(r) : t_bytesToHex(r)
            }

function t_bytesToHex(e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push((e[n] >>> 4).toString(16)),
                        t.push((15 & e[n]).toString(16));
                    return t.join("")
                }

d = function(e) {
            e._ts = (new Date).getTime() - 9999;
            var t, n = Object.keys(e), i = "", o = Object(c_a)(n.sort());
            try {
                for (o.s(); !(t = o.n()).done; ) {
                    var a = t.value;
                    void 0 !== e[a] && null !== e[a] && (i += "".concat(a, "=").concat(e[a], ","))
                }
            } catch (r) {
                o.e(r)
            } finally {
                o.f()
            }
            return [i,l(i)]
}

function get_sign(keyword){
    params = {
        "keyword": keyword,
        "page": 1,
        "limit": 12,
        "_platform": "web",
        "_versioin": "0.2.5"
    }
    return d(params)
}

console.log(get_sign("火车呼啸而过"))