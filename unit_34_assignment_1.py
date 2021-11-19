# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

def main(n):
    # 默认n为str
    ls = list(n)
    for i in range(4):
        ls[i] = str((int(ls[i]) + 5) % 10)
    ls[0], ls[3] = ls[3], ls[0]
    ls[1], ls[2] = ls[2], ls[1]
    return int("".join(ls))

if __name__ == "__main__":
    n = input("请输入")
    print(main(n))