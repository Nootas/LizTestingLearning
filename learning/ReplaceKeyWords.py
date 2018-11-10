'''
I also want to call this "wash your mouth with soap"
文件读取，字符串的运用
IO模块不用导入
首先得拥有一个写了关键词的txt
'''
userstring = input("remarks:")
print("checking...")

with open(r'sensitivewd.txt') as f:
    line = f.readline() #tip: this line include space & backspace
    key  = line.strip() #strip() is used to delete space & backspace in line I get
    for line in f: #遍历文件
        if key in userstring:
            userstring = userstring.replace(key,'*'*len(key)) #这里必须使用userstring迭代，以达到去除多个敏感词的目的
    print("Result: "+userstring) #这个print必须在文件关闭前打印，不然会打印原始输入内容
