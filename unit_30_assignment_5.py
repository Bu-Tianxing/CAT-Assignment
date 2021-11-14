# 【题目描述】 Armstrong数，就是n位数的各位数的n次方之和等于该数
# 如：153=1^3+5^3+3^3
# 1634=1^4+6^4+3^4+4^4
# 进阶版：给定范围（任意两数之间），求区间内的所有Armstrong数
def isArmstrong(n):
    lenth = len(str(n))
    # 分别计算每一位的三次方并加起来
    res = 0
    for i in range(1, lenth + 1):
        # temp是从右往左数第i位上的值，感觉这样写有点复杂，不知道有没有什么改进方法？
        temp = (n % (10 ** i)) // (10 ** (i - 1))
        res += temp ** lenth
    if n == res:
        return True
    else:
        return False

def main():
    ls = [int(i) for i in input("请输入两个数").split()]
    left = ls[0]
    right = ls[1]
    for j in range(left + 1, right):
        if isArmstrong(j):
            print(j)

if __name__ == "__main__":
    main()