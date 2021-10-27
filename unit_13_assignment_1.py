# 题目：D进制的A+B
# 题目描述：输入两个非负10进制整数A和B(<=230-1)，输出A+B的D (1 < D <= 10)进制数。
# 输入格式：输入在一行中依次给出3个整数A、B和D。
# 输出格式：输出A+B的D进制数。
# 输入样例： 123 456 8
# 输出样例： 1103

def main():
    ls = input("请输入").split()
    A, B, D = ls[0], ls[1], ls[2]
    A, B, D = int(A), int(B), int(D)
    LSres = list()
    sum_ = A + B
    res = ""
    if D > 10 and D <= 1:
        print("请检查输入")
        return 0
    while True:
        shang = sum_ // D #商
        yushu = sum_ % D #余数
        LSres.append(yushu)
        if shang == 0:
            break
        sum_ = shang
    LSres.reverse()
    return "".join(str(i) for i in LSres)

if __name__ == "__main__":
    print(main())

# 反思：
# 小错误有点多，虽然都能自己改过来，但考试的时候不跑代码有些错误可能看不出来，数据类型啥的得考虑清楚。