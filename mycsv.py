'''
练习写csv文件。
注意命名的时候不能命名成csv.py，不然运行时会与python自带的csv模块冲突。
int与string的转换
ASCII与char的转换
在MAC中运行使用 python3 
'''
import csv

TaeCSV = open('TaeCSV.py','w',encoding='utf-8',newline='') #首先创建一个文件
writer = csv.writer(TaeCSV) #定义一只笔，写入文件对象中
writer.writerow(['Archives'])#写入一行,以列表的方式
writer.writerow(['name','rank'])
i = 0
while i < 5:
    num=65+i
    name = 'Agent '+chr(num) #chr: ASCII 转字母
    rank = 'A'+str(i)
    writer.writerow([name,rank])
    i = i+1

TaeCSV.close()#写完后关闭文件

