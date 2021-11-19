# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

# 一般化 n个人 报到x退出，求剩下人的编号（编号为1-n）
def main(n, x):
    # 0 号位只占个格子
    ls = [True for i in range(n + 1)]
    out = 0
    check = 1
    while out != n - 1:
        for i in range(1, n + 1):
            if ls[i]:
                if check == x:
                    check = 1
                    out += 1
                    ls[i] = False
                    if out == n - 1:
                        break
                else:
                    check += 1
    ls[0] = False
    for i in ls:
        if i:
            return ls.index(i)

if __name__ == "__main__":
    n = int(input("n = ?"))
    x = int(input("x = ?"))
    print(main(n, x))