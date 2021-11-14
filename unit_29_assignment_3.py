# 二分查找解决找x的下标
# 【题目描述】 输入一个数n，然后输入n个数值各不相同，再输入一个值x，输出这个值在这个数组中的下标（从0开始，若不在数组中则输出-1）。
# 【输入】测试数据有多组，输入n(1<=n<=200)，接着输入n个数，然后输入x。
# 【输出】对于每组输入,请输出结果。
# 【样例输入】
# 4
# 1 2 3 4
# 3
# 【样例输出】
# 2

def binarySearch(n, Array, target):
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if Array[mid] == target:
            return mid
        elif Array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def main():
    n = int(input("n = ?"))
    ls = [int(i) for i in input("Array = ?").split()]
    target = int(input("target = ?"))
    print(binarySearch(n, ls, target))

if __name__ == "__main__":
    main()