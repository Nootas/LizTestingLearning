'''
python IO
open 位于IO模块，但IO模块是自动导入的，无需人为导入
应该是用with时，调用file.closed,不是用with时，使用file.close()
这里是读取某一个文件的前三行内容
'''

with open(r'/path/something.txt') as file:
    i=0
    for i in range(3):
        print(file.readline(),end='') #加一个print用来输出读取到的内容
    file.closed
