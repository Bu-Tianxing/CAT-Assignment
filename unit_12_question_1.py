# 题目：图像旋转 题目描述：旋转是图像处理的基本操作，
# 在这个问题中，你需要将一个图像逆时针旋转90度。计算机中的图像表示可以用一个矩阵来表示，
# 为了旋转一个图像，只需要将对应的矩阵旋转即可。
# 输入格式：输入的第一行包含两个整数 n, m，
# 分别表示图像矩阵的行数和列数。接下来n行每行包含m个整数，表示输入的图像。

def main():
    n, m = [int(k) for k in input("n=?\nm=?").split()]
#   mtx = [[1, 5, 3],
#          [3, 2, 4]] # 整数矩阵 (原做法)
    mtx = []
    for s in range(n):
        line = [int(k) for k in input("请输入第%d行"%(s+1)).split()]
        mtx.append(line)
    for j in range(m - 1, -1, -1):
        for i in range(n):
            print(mtx[i][j], end = " ")
        print()

if __name__ == "__main__":
    main()

# 反思：
# 列表推导式 [fun(k) for i in fun()]
# 列表里面可以放列表（核心思想）
# print()自带换行，print("\n")会导致空一行(相当于输入了两个换行符）
# print( end = " ")类似的用法还有sep = ""(设置间隔符）
# https://blog.csdn.net/sinat_28576553/article/details/81154912 （print用法）
# https://blog.csdn.net/SL_logR/article/details/81515086 （map函数解此题）