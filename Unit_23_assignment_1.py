# 汉诺塔问题: n个盘子要从a到c，有abc三个柱子

def move(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)

if __name__ == "__main__":
    n = int(input("n = ?"))
    from_ = input("from = ?")
    to_ = input("to = ?")
    temp_ = input("temp = ?")
    move(n, from_, temp_, to_)