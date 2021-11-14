# 约瑟夫生者死者小游戏
# 【题目描述】 30 个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。如此循环，直到船上仅剩15人为止，问都有哪些编号的人下船了呢？

# 进阶版： m个人，报到n下船，留k个人。求下船人的编号（从1开始）

def solve(m, n, k):
    # True/False 区分目前是否在船上，0号位占个格子，使列表序号和编号一致，后续不对0号位进行遍历
    numbs = [True for i in range(m + 1)]
    # 下船人数
    count = 0 # 统计已下船人数
    check = 1 # 从1开始报数
    while count != m - k: # 若下船人数未达到要求则继续进行
        for i in range(1, m + 1): # 完成一轮即为转了一圈（1-m）
            if count == m - k:
                break
            if numbs[i]: # 若已下船，直接下一位 （只有在船上才进行操作）
                if check == n: # 检查当前报的数是否为n
                    numbs[i] = False
                    check = 1
                    count += 1 # 是的话 1.修改目标状态 2.重置当前报数 3.下船人数+1
                else:
                    check += 1 # 否的话 当前报的数+1
    # 达到要求后会自动跳出循环，此时检查numbs即可得到下船人的编号
    result = []
    for j in range(1, m + 1): # 特别注意，numbs的0号位没有意义，永远不参与运算
        if not numbs[j]:
            result.append(j)
    return result

def main():
    ls = [int(i) for i in input("m, n, k = ?").split()]
    m, n, k = ls[0], ls[1], ls[2]
    print(solve(m, n, k))

if __name__ == "__main__":
    main()