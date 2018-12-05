import requests
from common import Fahrenheit2Degree,GenerateWeaterTime

location = {'latitude':39.88,'longtitude':-121.56} #北纬，东经
host = 'https://api.darksky.net'
method = '/forecast'
key = '123456789abcdefg987654321'
headers = {'content-encoding':'utf-8','content-type':'application/json'}

url = host+method+'/'+key+'/{0},{1}'.format(location['latitude'],location['longtitude'])
#for reduce latency and saving cache need optional params in http query string
betterURL = url+'?exclude=minutely,hourly,daily,alerts,flags&lang=zh' 
r = requests.get(betterURL,headers=headers,timeout=10)

if r.status_code == 200:
    weatherdict = r.json()

    timezone = weatherdict.get('timezone')
    current = weatherdict.get('currently').get('time') #get timestamp in UNIX form
    time = GenerateWeaterTime(current)  
    summary = weatherdict.get('currently').get('summary')
    Fahrenheit  = weatherdict.get('currently').get('temperature')
    Degree  = Fahrenheit2Degree(Fahrenheit)

    print("时区:{0}\n更新时间:{1}\n当前气温:{2}℃\n描述:{3}".format(timezone,time,Degree,summary))

else:
    print('接口访问失败，状态码：%s'%(r.status_code))
