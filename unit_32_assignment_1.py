# 【题目描述】 月饼是中国人在中秋佳节时吃的一种传统食品，不同地区有许多不同风味的月饼。
# 现给定所有种类月饼的库存量、总售价、以及市场的最大需求量，请你计算可以获得的最大收益是多少。
# 【输入格式】 每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N表示月饼的种类数、
# 以及不超过500（以万吨为单位）的正整数D表示市场最大需求量。随后一行给出N 个正数表示每种月饼的库存量（以万吨为单位）；
# 最后一行给出N个正数表示每种月饼的总 售价（以亿元为单位）。数字间以空格分隔。
# 【输出格式】 对每组测试用例，在一行中输出最大收益，以亿元为单位并精确到小数点后2位。
# 【输入样例】
# 3 20
# 18 15 10
# 75 72 45
# 【输出样例】
# 94.50

def main():
    n, need = [int(i) for i in input("几种月饼？需求量多大").split()]
    size = [float(i) for i in input("请输入每种月饼的数量").split()]
    price = [float(i) for i in input("请输入每种月饼的总价").split()]
    money = 0
    rate = {i: price[i] / size[i] for i in range(n)}
    # 字典：按输入顺序01234作为key，单价作为value
    # 得到一个列表，记录了单价从高到底排好序的输入顺序的索引
    order = sorted(rate, key = lambda i: rate[i], reverse=True)
    # i 的值即为order[0],order[1]。。。按顺序的值（这里的实际意义就是 盈利高到低的月饼的 输入序号）
    for i in order:
        if need <= size[i]:
            money += (rate[i] * need)
            break
        else:
            money += price[i]
            need -= size[i]
    print("最高可卖%.2f亿元"%money)
    return money

if __name__ == "__main__":
    main()