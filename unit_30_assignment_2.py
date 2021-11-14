# 菲波那切数列递归实现

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    n = int(input("n = ?"))
    print(fib(n))