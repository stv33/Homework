import requests
import time  #获取时间戳
import json
import matplotlib.pyplot as plt    #绘图库
import sqlite3         #sqlite数据库
# 获取 时间戳
def gettime():
    return int(round(time.time() * 1000))

if __name__ == '__main__':
    # 用来自定义头部的
    headers = {}
    # 用来传递参数
    keyvalue = {}
    # 目标网址
    url = 'http://data.stats.gov.cn/easyquery.htm'

    # 头部的填充
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) ' \
                            'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                            'Version/12.0 Safari/605.1.15'

    # 下面是参数的填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}]'
    keyvalue['k1'] = str(gettime())

    # 发出请求，使用get方法
    # 建立一个Session,在Session基础上进行一次请求
    s = requests.session()
    r = s.get(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"2000}]'
    r = s.get(url, params=keyvalue, headers=headers)
    print (r.status_code)
