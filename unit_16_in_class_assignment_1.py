# 题目描述：甲乙丙丁决定玩一个报数的游戏来打发时间.
# 游戏规则为四个人从1开始轮流进行报数，但如果需要报出的数是7的倍数或含有数字7则直接跳过。
# 此外大家约定，在总共报出了n个数后（不计入被跳过的数）游戏结束。
# 现在需要你来帮忙统计，游戏过程中每个人各自跳过了几次。
# 输入格式：从标准输入读入数据。输入仅一行，包含一个正整数n，表示报出了多少个数后游戏结束。
# 输出格式：输出到标准输出。
# 输出共四行，每行一个整数，以此表示甲乙丙丁四人在游戏过程中跳过的次数。

def main():
    # n = int(input("n=? "))
    # ls = [i for i in range(n+1)]
    # jia, yi, bing, ding = 0, 0, 0, 0
    # for j in range(1, n+1):
    #     if j % 7 == 0 or "7" in list(str(j)):
    #         ls[j] = 0
    # for a in range(1, n+1, 4):
    #     if ls[a] == 0:
    #         jia += 1
    # for b in range(2, n+1, 4):
    #     if ls[b] == 0:
    #         yi += 1
    # for c in range(3, n+1, 4):
    #     if ls[c] == 0:
    #         bing += 1
    # for d in range(4, n+1, 4):
    #     if ls[d] == 0:
    #         ding += 1
    # print(jia, yi, bing, ding)
    # return 0
    n = int(input("n=? "))
    ls = [0 for i in range(4)]
    total_number = 0
    number = 1
    while total_number <= n:
        if number % 7 == 0 or "7" in str(number):
            ls[(number % 4) - 1] += 1
        else:
            total_number += 1
        number += 1
    for i in range(4):
        print(ls[i])

if __name__ == "__main__":
    main()

# 反思：
# 一开始以为n是到多少为止，看错题意了，应该是报了n个数为止（跳过的不算）