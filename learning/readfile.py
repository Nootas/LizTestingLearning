'''
python IO
open 位于IO模块，但IO模块是自动导入的，无需人为导入
应该是用with时，调用file.closed,不是用with时，使用file.close()
这里是读取某一个文件的演示
'''

#读取一个文件内的所有内容
with open(r'/path/itext.txt') as file:
    while True:
        line = file.readline().strip() #readline 自带\n 所以strip()处理一下
        if line:
            print(line) #print 也自带\n
        else:
            break
            
#读取一个文件的前三行内容
with open("/path/something.txt",'r') as f:
    i = 0
    for i in range(3):
        print(f.readline(), end='') #在print里末尾传递空能够消除print自带的\n
    file.closed
        
            
    
