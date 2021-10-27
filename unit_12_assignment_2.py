# 题目描述：在一个整数序列 a 1, a 2, …, a n 中，如果存在某个数，大于它的整数数量等于小于它的整数数量，则称其为中间数。
# 在一个序列中，可能存在多个下标不相同的中间数，这些中间数的值是相同的。
# 输入格式：输入的第一行包含了一个整数 n ，表示整数序列中数的个数。
# 第二行包含n个正整数，依次表示a 1, a 2, …, a n。
# 输出格式：如果约定序列的中间数存在，则输出中间数的值，否则输出-1表示不存在中间数。

def main():
    n = int(input("n=? "))
    numbs = [int(s) for s in input("please give me some numbers").split()]

    # solution 1
    # numbs.sort()

    # solution 2
    for i in range(n-1):
        for j in range(1, n):
            if n - i >= j and numbs[j] <= numbs[j-1]:
                numbs[j], numbs[j-1] = numbs[j-1], numbs[j]

    if n % 2 == 0:
        if numbs[n//2] == numbs[n//2-1] and numbs.count(numbs[n//2]) % 2 == 0:
            return numbs[n//2]
        return -1
    else:
        return numbs[n//2]

if __name__ == "__main__":
    print(main())

# 全自己想的，感觉判断逻辑复杂了，有点繁琐。
# 先是分成奇偶，奇数好办就直接返回中间数，偶数的话需要判断中间两位是否一样
# 再判断中间两位的数一共有几个，如果也是偶数个的话再返回中间值
# Question：sort()方法算不算作弊啊，感觉这是用python自带的函数实现了大小排序功能
# https://www.cnblogs.com/onepixel/articles/7674659.html