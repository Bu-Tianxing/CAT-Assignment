# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.
# 编程找出1000以内的所有完数。（提示：分解因数）
def wanshu(n):
    if n < 1:
        print("您输入的数字有误。")
        return False
    if n == 1:
        return True
    yinzi = list()
    for i in range(1, n):
        if n % i == 0:
            yinzi.append(i)
    if n == sum(yinzi):
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(1, 1001):
        if wanshu(i):
            print("%d是完数。"%i)

# 反思：
# 并不知道1不算完数，1的逻辑写错了，应该False。
# 还是选择了用列表来存放因子然后直接sum对列表求和，应该学会用变量的方法在每次循环中存放这些因子的和。
# 没有注意到其实循环到n//2+1即可停止，有点浪费算力。