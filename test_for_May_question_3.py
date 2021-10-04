# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等 于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋ 3的三次方。

for i in range(100,1000):
    a = i // 100
    b = (i-a*100) // 10
    c = i % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print("%d是一个水仙花数"%i)

# 反思：
# 这题比较简单，没啥疑问，就是每题都要搞成 def xxfunction() 最后编一个main入口 xxfunction()吗？