# 题目：最大公约数
# 题目描述：输入两个正整数，求其最大公约数。
# 输入格式：测试数据有多组，每组输入两个正整数。
# 输出格式：对于每组输入,请输出其最大公约数。
# 输入样例：49 14
# 输出样例：7

def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

if __name__ == "__main__":
    ls = [int(i) for i in input("请输入").split()]
    print(gcd((ls[0]), (ls[1])))