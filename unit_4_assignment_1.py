# 输出九九乘法表
print ("这是一个九九乘法表：")
for i in range(1,10):
    for k in range(1,10):
        if i<=k:
            result=i*k
            print(i, "x", k, "=", result)