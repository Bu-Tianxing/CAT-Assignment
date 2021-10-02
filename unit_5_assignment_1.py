# 一般方法
def fahrenheit(c):
    return c * 1.8 + 32

# lambda方法
f = lambda c: c * 1.8 + 32

#检验是否相等
f1 = fahrenheit(30)
f2 = f(30)
print(f1)
print(f2)
if f1 == f2:
    print(True)
else:
    print(False)