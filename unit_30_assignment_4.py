# 【题目描述】 Armstrong数，就是n位数的各位数的n次方之和等于该数
# 如：153=1^3+5^3+3^3
# 1634=1^4+6^4+3^4+4^4
# 基础版：限定三位数，判断是不是Armstrong数

def isArmstrong(n):
    # 分别计算百位，十位，个位
    bai = n // 100
    shi = (n % 100) // 10
    ge = n - bai * 100 - shi * 10
    if n == (bai ** 3) + (shi ** 3) + (ge ** 3):
        return True
    return False

if __name__ == "__main__":
    n = int(input("n = ?"))
    if isArmstrong(n):
        print("%d是Armstrong数"%n)
    else:
        print("%d不是Armstrong数"%n)