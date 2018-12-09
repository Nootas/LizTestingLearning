#__*__coding:utf-8__*__

import requests
from common import Fahrenheit2Degree,GenerateWeaterTime
import readconfig as readconfig

method = '/forecast'

loadreadconfig = readconfig.ReadConfig()
host = loadreadconfig.get_host('Host')
key  = loadreadconfig.get_key('Key')
latitude   = loadreadconfig.get_latitude('Latitude')
longtitude = loadreadconfig.get_longtitude('Longtitude')

headers = {'content-encoding':'utf-8', 'content-type':'application/json'}

URL  = host+method+'/'+key+'/{0},{1}'.format(latitude, longtitude)
#for reduce latency and saving cache need optional params in http query string
BURL = URL+'?exclude=minutely,hourly,alerts,flags&lang=zh'  #BetterURL
rqst = requests.get(BURL, headers=headers, timeout=10)

if rqst.status_code == 200:
    weatherdict  = rqst.json()

    timezone = weatherdict.get('timezone')
    current  = weatherdict.get('currently').get('time')  #得到的是UNIX格式的时间戳
    time     = GenerateWeaterTime(current)  #转换成正常的时间
    summary  = weatherdict.get('currently').get('summary')
    Faht     = weatherdict.get('currently').get('temperature')  #Fahrenheit
    Degree   = Fahrenheit2Degree(Faht)
    print("时区:{0}\n更新时间:{1}\n当前气温:{2}℃\n描述:{3}".format(timezone, time, Degree, summary))

    daily    = weatherdict.get('daily').get('summary')
    futime   = weatherdict.get('daily').get('data')[0].get('time')
    fotime   = GenerateWeaterTime(futime)
    smry     = weatherdict.get('daily').get('data')[0].get('summary')
    Thigh    = weatherdict.get('daily').get('data')[0].get('temperatureHigh')
    Tlow     = weatherdict.get('daily').get('data')[0].get('temperatureLow')
    ThighinD = Fahrenheit2Degree(Thigh)
    TlowinD  = Fahrenheit2Degree(Tlow)
    print("天气预测:{0}\n时间:{1}\n描述:{2}\n最高温度:{3}\n最低温度:{4}".format(daily, fotime, smry, ThighinD, TlowinD))

else:
    print('接口访问失败，状态码：%s'%(r.status_code))

