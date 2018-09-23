'''
PYthon IO
open 位于IO模块，但IO模块是自动导入的，无需人为导入
'''

with open(r'/Users/otae/Desktop/TaePython/something.txt') as file:
    i=0
    for i in range(3):
        print(file.readline(),end='')
    file.close()
