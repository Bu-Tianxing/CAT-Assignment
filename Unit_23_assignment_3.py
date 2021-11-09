# 递归求阶乘

def jc(n):
    if n < 0:
        print("您输入有误")
    elif n <= 1:
        return 1
    else:
        return n * jc(n-1)
if __name__ == "__main__":
    res = jc(int(input("n = ?")))
    print(res)