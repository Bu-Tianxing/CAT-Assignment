# fib 数列求和：递归算法

def fib(n):
    if n < 0:
        print("您输入有误")
    elif n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
if __name__ == "__main__":
    res = fib(int(input("n = ?")))
    print(res)