# 题目描述：某市设有 n 个核酸检测点，编号从1到 n,其中i号检测点的位置可以表示为一个平面整数坐标(xi, yi)。为方便预约核酸检测，请根据市民所在位置(x, y) ，查询距其最近的三个检测点。
# 多个检测点距离相同时，编号较小的视为更近。
# 输入格式：输入共 n + 1 行。
# 第一行包含用空格分隔的三个整数 n、x 和 y，表示检测点总数和市民所在位置。
# 第二行到第 n + 1 行依次输入 n 个检测点的坐标。
# 第 i + 1 行（1<= i <= n）包含用空格分隔的两个整数xi和yi,表示i号检测点所在位置。

def main():
    ls = [int(i) for i in input("请输入").split()]
    distance = []
    for j in range(ls[0]):
        coordination = [int(i) for i in input("请输入坐标").split()]
        dis = (ls[1] - coordination[0]) ** 2 + (ls[2] - coordination[1]) ** 2
        distance.append((dis, j + 1))
    distance.sort()
    for s in range(ls[0]):
        print(distance[s][1])
    return 0

if __name__ == "__main__":
    main()

# 反思：
# 这题花了我一个半小时才搞懂
# map函数能很方便的输入多个变量，不用搞一个列表存放了。
# 有字典的解法，但字典的用法不够熟练，字典作为无序数据类型，排序也很麻烦