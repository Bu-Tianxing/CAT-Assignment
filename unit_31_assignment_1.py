# 求一个整数的所有因数

def getFactor(n):
    res = []
    count = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            res.append(i)
            count += 1
    print("%d共有%d个因数"%(n, count))
    print("他们分别是：", end = "")
    for j in range(len(res)):
        print(res[j], end = " ")
    return res

if __name__ == "__main__":
    n = int(input("n = ?"))
    getFactor(n)