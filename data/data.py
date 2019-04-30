import json
import matplotlib.pyplot as plt    #绘图库
import sqlite3         #sqlite数据库
import requests
import time  #获取时间戳

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
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}]'
    keyvalue['k1'] = str(gettime())

    # 发出请求，使用get方法
    # 建立一个Session,在Session基础上进行一次请求
    s = requests.session()
    r = s.get(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    r = s.get(url, params=keyvalue, headers=headers)
    #解析数据
    year = [] #年份
    int_year = []#整数形式的年份列表
    population = [] #年末总人口
    population_man = [] #年末男性总人口
    population_woman = [] #年末女性总人口
    ratio_man = [] #男人口占比
    ratio_woman = [] #女人口占比
    data_unhandle = json.loads(r.text)
    data= data_unhandle['returndata']['datanodes']
    for i in range(1999,2019):
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
        for value in data_i: #若使用爬虫则改为data_i
            if ('A030101_sj' in value['code']):
                year.append(value['code'][-4:])
                population.append(int(value['data']['strdata']))
            if ('A030102_sj' in value['code']):
                population_man.append(int(value['data']['strdata']))
            if ('A030103_sj' in value['code']):
                population_woman.append(int(value['data']['strdata']))
    list.reverse(population)
    list.reverse(population_man)
    list.reverse(population_woman)
    list.reverse(year)
    for i in range(1999,2019):
        int_year.append(i)
    print(year)
    print(int_year)
    print(population)
    print(population_man)
    print(population_woman)

#定义类来储存每一年的各项数据
    year_table=[]

    class year_information(object):
        def __init__(self,year_int,P,M,F):
            self.year_str=str(year_int)
            self.Pstr=str(P)
            self.Mstr=str(M)
            self.Fstr=str(F)
            self.MRatio=str(M/P)
            self.FRatio=str(F/P)
            self.yearP = '('+ self.Pstr +','+ self.year_str + ')'
            self.yearM = '('+ self.Mstr +','+ self.year_str + ')'
            self.yearF = '('+ self.Fstr +','+ self.year_str + ')'
            self.yearMR = '('+ self.MRatio +','+ self.year_str + ')'
            self.yearFR = '('+ self.FRatio +','+ self.year_str + ')'

    for i in range(0,20):
        temp = year_information(int_year[i],population[i],population_man[i],population_woman[i])
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
    cu.execute('CREATE TABLE year_p_man (population , year UNIQUE)')
    cu.execute('CREATE TABLE year_p_woman (population , year UNIQUE)')
    cu.execute('CREATE TABLE year_R_man (ratio , year UNIQUE)')
    cu.execute('CREATE TABLE year_R_woman (ratio , year UNIQUE)')
    for i in range(0,20):
        cu.execute('INSERT INTO year_population VALUES ' + year_table[i].yearP)
        cu.execute('INSERT INTO year_p_man VALUES '+ year_table[i].yearM)
        cu.execute('INSERT INTO year_p_woman VALUES '+ year_table[i].yearF)
        cu.execute('INSERT INTO year_R_man VALUES'+ year_table[i].yearMR)
        cu.execute('INSERT INTO year_R_woman VALUES'+ year_table[i].yearFR)
    conn.commit()

#从数据库里读取数据
    year_read = []
    P_read=[]
    M_read=[]
    F_read=[]
    MR_read=[]
    FR_read=[]
#读取年份和总人口
    cu.execute("SELECT * FROM year_population")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        year_read.append(temp[1])
        P_read.append(temp[0])
#读取男性人口 
    cu.execute("SELECT * FROM year_p_man")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        M_read.append(temp[0])
#读取女性人口    
    cu.execute("SELECT * FROM year_p_woman")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        F_read.append(temp[0])
#读取男性占比    
    cu.execute("SELECT * FROM year_R_man")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        MR_read.append(temp[0])
#读取女性占比    
    cu.execute("SELECT * FROM year_R_woman")
    res = cu.fetchall()
    for value in res:
        temp = eval(str(value))
        FR_read.append(temp[0])
    
    print(MR_read)

#绘制数据图表
#总人口图
    fig1=plt.figure(figsize=(10,6))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(year_read, P_read)
    plt.xlabel(u'年份')
    plt.ylabel(u'万人')
    plt.title(u'年末总人口')

#男女比折线图
    fig2=plt.figure(figsize=(10,6))
    plt.ylim((0.47, 0.53))
    plt.xticks(year_read)
    line_man = plt.plot(int_year, MR_read,color = 'green',linewidth = 2.0, linestyle = '--')
    line_woman = plt.plot(int_year, FR_read,color = 'purple',linewidth = 3.0, linestyle = '-.')
    plt.legend( labels=['男', '女'],loc='upper right')
    plt.xlabel(u'年份')
    plt.ylabel(u'比例')
    plt.title(u'男女占比折线图')
    plt.show()

    conn.close()




