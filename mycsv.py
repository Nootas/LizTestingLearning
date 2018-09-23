'''
练习写csv文件。
注意命名的时候不能命名成csv.py，不然运行时会与python自带的csv模块冲突。
int与string的转换
'''
import csv

testfile = open('tae.csv','w',newline='')
writer = csv.writer(testfile)
writer.writerow(['name','sex','phone'])
i=0
while i<4:
    name = "Agent "+str(i)
    if i%3 == 0:
        sex = "woman"
    else:
        sex = "man"
    writer.writerow([name,sex,'188xxxx1876'])
    i=i+1

testfile.close()
