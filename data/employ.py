import json
import matplotlib.pyplot as plt    #绘图库
import sqlite3         #sqlite数据库
import requests
import time  #获取时间戳
import numpy as np

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
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
                            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome'\
                            '74.0.3729.108 Safari/537.36'

    # 下面是参数的填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0402"}]'
    keyvalue['k1'] = str(gettime())

    # 发出请求，使用get方法
    # 建立一个Session,在Session基础上进行一次请求
    s = requests.session()
    #解析数据
    year = [] #年份
    int_year = []#整数形式的年份列表
    population = [] #就业人员
    population_1 = [] #第一产业就业人员
    population_2 = [] #第二产业就业人员
    population_3 = [] #第三产业就业人员
    ratio_1 = [] #第一产业就业人员占比
    ratio_2 = [] #第二产业就业人员占比
    ratio_3 = [] #第三产业就业人员占比
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0402"}]'
    r = s.get(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    r = s.get(url, params=keyvalue, headers=headers)
    for i in range(1999,2018):
        time.sleep(1)#防ip被封
        # 修改dfwds字段内容
        str1='[{"wdcode":"sj","valuecode":'
        str2=str(i)
        str3='}]'
        keyvalue['dfwds'] = str1+str2+str3
        # 再次进行请求
        r = s.get(url, params=keyvalue, headers=headers)
        data_handle = json.loads(r.text)
        data_i = data_handle['returndata']['datanodes']
        print(data_handle)
        for value in data_i:
            if ('A040201_sj' in value['code']):
                year.append(value['code'][-4:])
                population.append(float(value['data']['strdata']))
            if ('A040202_sj' in value['code']):
                population_1.append(float(value['data']['strdata']))
            if ('A040203_sj' in value['code']):
                population_2.append(float(value['data']['strdata']))
            if ('A040204_sj' in value['code']):
                population_3.append(float(value['data']['strdata']))

    for i in range(1999,2018):
        int_year.append(i)
    print(year)
    print(int_year)
    print(population)
    print(population_1)
    print(population_2)
    print(population_3)
#定义类来储存每一年的各项数据
    year_table=[]

    class year_information(object):
        def __init__(self,year_int,P,P1,P2,P3):
            self.year_str=str(year_int)
            self.Pstr=str(P)
            self.P1str=str(P1)
            self.P2str=str(P2)
            self.P3str=str(P3)
            self.Ratio1=str(P1/P)
            self.Ratio2=str(P2/P)
            self.Ratio3=str(P3/P)
            self.yearP = '('+ self.Pstr +','+ self.year_str + ')'
            self.yearP1 = '('+ self.P1str +','+ self.year_str + ')'
            self.yearP2 = '('+ self.P2str +','+ self.year_str + ')'
            self.yearP3 = '('+ self.P3str +','+ self.year_str + ')'
            self.yearR1 = '('+ self.Ratio1 +','+ self.year_str + ')'
            self.yearR2 = '('+ self.Ratio2 +','+ self.year_str + ')'
            self.yearR3 = '('+ self.Ratio3 +','+ self.year_str + ')'

    for i in range(0,19):
        temp = year_information(int_year[i],population[i],population_1[i],population_2[i],population_3[i])
        year_table.append(temp)

#保存数据至数据库
    input_str = input("Input DATABASE Name:")
    str_stand = input_str + '.db'
    conn = sqlite3.connect(str_stand)
    # 创建一个Cursor:
    cu = conn.cursor()
    #创建年份——人口表格
    cu.execute('CREATE TABLE year_population (population , year UNIQUE)')
    #创建年份——男,女人口表格
    cu.execute('CREATE TABLE year_p_1 (population , year UNIQUE)')
    cu.execute('CREATE TABLE year_p_2 (population , year UNIQUE)')
    cu.execute('CREATE TABLE year_p_3 (population , year UNIQUE)')
    cu.execute('CREATE TABLE year_R_1 (ratio , year UNIQUE)')
    cu.execute('CREATE TABLE year_R_2 (ratio , year UNIQUE)')
    cu.execute('CREATE TABLE year_R_3 (ratio , year UNIQUE)')

    for i in range(0,19):
        cu.execute('INSERT INTO year_population VALUES ' + year_table[i].yearP)
        cu.execute('INSERT INTO year_p_1 VALUES '+ year_table[i].yearP1)
        cu.execute('INSERT INTO year_p_2 VALUES '+ year_table[i].yearP2)
        cu.execute('INSERT INTO year_p_3 VALUES '+ year_table[i].yearP3)
        cu.execute('INSERT INTO year_R_1 VALUES'+ year_table[i].yearR1)
        cu.execute('INSERT INTO year_R_2 VALUES'+ year_table[i].yearR2)
        cu.execute('INSERT INTO year_R_3 VALUES'+ year_table[i].yearR3)
    conn.commit()

#从数据库里读取数据
    year_read = []
    P_read=[]
    P1_read=[]
    P2_read=[]
    P3_read=[]
    R1_read=[]
    R2_read=[]
    R3_read=[]
#读取年份和总人口
    cu.execute("SELECT * FROM year_population")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        year_read.append(temp[1])
        P_read.append(temp[0])
#读取第一产业人口 
    cu.execute("SELECT * FROM year_p_1")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        P1_read.append(temp[0])
#读取第二产业人口    
    cu.execute("SELECT * FROM year_p_2")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        P2_read.append(temp[0])
#读取第三产业人口    
    cu.execute("SELECT * FROM year_p_3")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        P3_read.append(temp[0])
#读取第一产业人口占比    
    cu.execute("SELECT * FROM year_R_1")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        R1_read.append(temp[0])
#读取第二产业人口占比    
    cu.execute("SELECT * FROM year_R_2")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        R2_read.append(temp[0])
#读取第三产业人口占比    
    cu.execute("SELECT * FROM year_R_3")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        R3_read.append(temp[0])    


#绘制数据图表
#总就业人口图
    fig1=plt.figure(figsize=(10,6))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(year_read, P_read)
    plt.xlabel(u'年份')
    plt.ylabel(u'万人')
    plt.title(u'1999-2017年就业总人口')

#2017
    fig2=plt.figure(figsize=(10,6))
    plt.title('2017年第一、二、三产业占比饼状图')
    ratio_map = {
        '第一产业': (R1_read[18], '#7199cf'),
        '第二产业': (R2_read[18], '#4fc4aa'),
        '第三产业': (R3_read[18], '#e1a7a2')
    }
    data = [R1_read[18],R2_read[18],R3_read[18]]
    colors = [x[1] for x in ratio_map.values()]  #对应颜色
    ingredients = ["第一产业"+str(R1_read[18]),"第二产业"+str(R2_read[18]),"第三产业"+str(R3_read[18])]
    plt.pie(data, labels=ingredients, colors=colors)

    plt.show()

    conn.close()




