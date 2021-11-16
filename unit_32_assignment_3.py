# 使用贪心算法解决背包问题有一个背包，背包容量是M=150。 
# 有7个物品，物品可以分割成任意大小。要求尽可能让装入背包中的物品总价值最大，但不能超过总容量。返回总价值
# 物品 A  B  C  D   E  F  G
# 重量 35 30 60 50 40 10 25
# 价值 10 40 30 50 35 40 30
# 进阶版：N种物品，重量、价值分别用weight（列表）和price（列表）表示，背包总容量D 并打印装货方案
def solve(N, weight, price, D):
    rate = {i: price[i] / weight[i] for i in range(N)}
    order = sorted(rate, key=lambda i: rate[i], reverse=True)
    value = 0
    for i in order:
        if weight[i] >= D:
            print("第%d种物品装%.2f"%(i+1, D))
            value += rate[i] * D
            break
        else:
            D -= weight[i]
            value += price[i]
            print("第%d种物品装%.2f"%(i+1, weight[i]))
    return value

if __name__ == "__main__":
    N = int(input("请输入物品个数"))
    weight = [float(i) for i in input("请按顺序输入总重量").split()]
    price = [float(i) for i in input("请按顺序输入总价值").split()]
    D = int(input("请输入背包容量"))
    print("总价值为%.2f"%solve(N, weight, price, D))