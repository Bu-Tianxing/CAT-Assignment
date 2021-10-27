# 题目：求和（1）（2019真题）
# 题目描述：输入一个正整数a和正整数n，求s=a+aa+aaa+aaaa+aa…a (n个a)的值;
# 输入格式：测试数据输入两个正整数。
# 输出格式：对于每组输入,请输出s=a+aa+aaa+aaaa+aa…a (n个a)的值。
# 输入样例：1 3
# 输出样例：123

def main():
    data = [int(i) for i in input("请输入").split()]
    a, n = data[0], data[1]
    ls = [a]
    for j in range(n-1):
        ls.append(ls[-1] * 10 + a)
    return sum(ls)

if __name__ == "__main__":
    print(main())