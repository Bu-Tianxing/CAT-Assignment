# 【题目描述】 题目：有两个磁盘文件A和B,各存放一行字母，
# 要求把这两个文件中的信息合并（按字母顺序排列），输出到一个新文件C中。
# 假设有 A.txt B.txt 两个文件

f = open("A.txt", "r", encoding="utf-8")
print(f.name) # f.name后面不用括号
line = f.read(10) #读取前十个字符
f.readline() #读取第一行
f.readline(5) #读取第二行的前5个字符
f.close() #关闭文件
a = "1234"
f.write(a)