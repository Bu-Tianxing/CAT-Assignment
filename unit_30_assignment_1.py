# C 语言练习实例1
# 19年真题
# 【题目描述】有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数? 都是多少？

def threenums():
    nums = []
    count = 0
    for i in range(1,5):
        for j in range(1,5):
            for s in range(1,5):
                if i != j and i != s and j != s:
                    num = i * 100 + j * 10 + s
                    count += 1
                    nums.append(num)
    return count, nums

if __name__ == "__main__":
    print(threenums())