# 求0—7所能组成的奇数个数。

def main():
    temp, sum = 4, 4
    # 1位只有四种情况1 3 5 7，所以初始化sum为4，temp用于记录i位数的情况，也默认已经乘上个位的情况（4种）
    # 从2位数起开始算
    for i in range(2, 9):
        if i == 2: # 若在首位只能1-7
            temp *= 7
        else: # 不在首位可以0-8
            temp *= 8
        sum += temp
    return sum

if __name__ == "__main__":
    print(main())