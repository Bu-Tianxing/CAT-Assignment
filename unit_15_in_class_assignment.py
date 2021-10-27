# 题目描述：令P表示第i个素数，现任意给两个正整数M≤N≤10^4，请输出PM到PN的所有素数。
# 输入格式：输入在一行中给出M和N,其间以空格分隔。
# 输出格式：输出从PM~PN的所有素数,每10个数字占1行,其间以空格分隔，但行末不得有多 余空格。
# 输入样例：5 27
# 输出样例：
# 11 13 17 19 23 29 31 37 41 43
# 47 53 59 61 67 71 73 79 83 89
# 97 101 103

def prime(m, n):
    if m > n:
        m, n = n, m
    prime_list =[0]
    is_right = [True] * (10 ** 4)
    is_right[0], is_right[1] = False, False
    for i in range(10 ** 4):
        if is_right[i]:
            for j in range(i ** 2, 10 ** 4, i):
                is_right[j] = False
    numb = 0
    for s in range(10 ** 4):
        if is_right[s]:
            prime_list.append(s)
            numb += 1
            if numb == n:
                break
    for q in range(m, n+1):
        print(prime_list[q], end = " ")
        if (q - m + 1) % 10 == 0:
            print()

if __name__ == "__main__":
    [m, n] = [int(i) for i in input("请输入").split()]
    prime(m, n)

# 反思：
# 输出十个一行那里想了有一个小时，有点麻烦。