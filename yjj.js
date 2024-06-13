window = global
proxy_array = ['window','document','navigator','location']
var content = "arg1_content";
null_function = function (){console.log(arguments)}
delete __filename;
delete __dirname;


null_function = function (){console.log(arguments)}

window = global
window.top = window
window.setInterval = null_function
window.ActiveXObject = undefined
window.addEventListener = null_function

document = {
    characterSet:'UTF-8',
    charset:'UTF-8',
    scripts: ['script','script']
}
document.removeChild = null_function
div = {getElementsByTagName(val){
    if(val==='i'){ return {length :0}}
    }}
document.createElement = function (val){if(val==='div'){return div} if (val === 'form'){
        return {}
    } if (val === 'a'){
        return {}
    }}
document.getElementsByTagName = function (val){
        return [
            {
                content:content,
                parentNode:{
                    removeChild:function (){}
                },
                parentElement : {
                     removeChild:function (){}
                }
            },
            {
                 content:content,
                 parentNode:{
                    removeChild:function (){}
                },
                parentElement : {
                     removeChild:function (){}
                }
            }
        ]
}
document.getElementById = null_function

Object.prototype.getAttribute = function (val){if(val==='r'){return 'm'}}
location = {
    "ancestorOrigins": {},
    "href": "https://www.nmpa.gov.cn/datasearch/home-index.html",
    "origin": "https://www.nmpa.gov.cn",
    "protocol": "https:",
    "host": "www.nmpa.gov.cn",
    "hostname": "www.nmpa.gov.cn",
    "port": "",
    "pathname": "/datasearch/home-index.html",
    "search": "",
    "hash": ""
}
navigator = {
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    languages: ["zh-CN", "zh"],
    appVersion: "5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    webdriver: false,
    appName: "Netscape",
    vendor: "Google Inc.",
    connection:  {
        downlink: 10,
        effectiveType: "4g",
        rtt: 200,
        saveData: false,
    }
}


"arg2_js";
require('./15QqdX9S7nDE')


function get_cookie(){
    return document.cookie
}
console.log(document.cookie);