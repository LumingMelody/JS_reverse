# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 17:46
# @Author  : 蔍鸣霸霸
# @FileName: py_jsparser.py
# @Software: PyCharm
# @Blog    ：只因你太美

# 完整代码如下，大家自己试试删除无用变量a吧！
# js2py依赖于pyjsparser，所以安装js2py即可安装pyjsparser
# pip install js2py

script = '''
    function sum(a,b){  
        c = minus(2,3)
        return a+c;
    };

    function minus(a2,b2){  
        return a2-b2;
    };

    function dddd(a2,b2){  
        return a2-b2;
    };

    var a = 123;
    sum(1,2)
'''

import pyjsparser

js_ast = pyjsparser.parse(script)
# 获取所有方法
funcList = []
for i in js_ast['body']:
    if i['type'] == 'FunctionDeclaration':
        name = i['id']['name']
        funcList.append(name)
# 查找未被调用的方法
noCallList = []
for func in funcList:
    searchStatement = "{'type': 'CallExpression', 'callee': {'type': 'Identifier', 'name': '%s'}" % func
    if searchStatement not in str(js_ast):
        noCallList.append(func)

# 删除未调用的方法
for i in js_ast['body']:
    if i['type'] == 'FunctionDeclaration':
        if i['id']['name'] in noCallList:
            js_ast['body'].remove(i)

# js_ast['body'][0]['id']['name'] = 'pythonlx'  # 修改一个函数名

# 用AST重新生成js代码
import js2py.py_node_modules.escodegen as escodegen

escodegen = escodegen.var.get('escodegen')
res = escodegen.get('generate')(js_ast)
print(res.to_python())
