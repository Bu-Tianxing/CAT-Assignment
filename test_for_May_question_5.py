# 求 s = a + a a + a a a + a a a a + a a . . . a 的 值 ， 其 中 a 是 一 个 数 字 。
# 例如 2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

def main(m, n):
    element = [0]
    for i in range(1, n + 1):
        tmp = m * (10 ** (i - 1))
        element.append(element[-1] + tmp)
    return sum(element)

if __name__ == "__main__":
    m = int(input("请输入被加的数字"))
    n = int(input("请输入加的个数"))
    print("相加结果为%d"%main(m, n))

# 反思:
# 忘记设置限定条件了，即0<=m<=9
# 没听答案的时候就自己运用了临时变量，但也只用了一个临时变量，没有把加数的结果也设置一个。
# 用了之前斐波那契数列的思想，用列表存放所有加数，然后调用最后一个，每次只需计算最大数位上的运算。