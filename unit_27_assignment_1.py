# 冒泡排序

def bubble_sort(Array):
    n = len(Array)
    for i in range(1, n):
        for j in range(n - i):
            if Array[j] > Array[j+1]:
                Array[j], Array[j+1] = Array[j+1], Array[j]
    return Array

if __name__ == "__main__":
    print(bubble_sort([2,3,54,1,35,6,31,5,321,8,52]))