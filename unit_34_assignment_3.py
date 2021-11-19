# 编程验证哥德巴赫猜想：任何一个不小于6的偶数均可表示为两个奇素数之和。
# 素数就是只能被1和自身整除的正整数。注意：1不是素数，2是素数。

from math import sqrt

# 用来判断n是不是素数
def isprime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 获得一个[1,n]内只含奇数的素数表
def getprimelist(n):
    res = []
    for i in range(3, n + 1):
        if isprime(i):
            res.append(i)
    return res

# 在ls里找到两数之和为x（ls为升序）
def FindTwoNumber(ls, x):
    L = len(ls)
    for i in range(L):
        for j in range(L):
            if ls[i] < x and ls[j] < x and ls[i] + ls[j] == x:
                return("%d = %d + %d" % (x, ls[j], ls[i]))
    return("%d是哥德巴赫猜想的反例"%x)

def main():
    n = int(input("请输入你要验证多少以内的哥德巴赫猜想"))
    ls = getprimelist(n)
    for i in range(6, n + 1, 2):
        if FindTwoNumber(ls, i):
            print(FindTwoNumber(ls, i))
    return 0

if __name__ == "__main__":
    main()