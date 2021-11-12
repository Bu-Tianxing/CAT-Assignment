# 选择排序

def select_sort(Array):
    n = len(Array)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if Array[j] < Array[min_index]:
                min_index = j
        Array[i], Array[min_index] = Array[min_index], Array[i]
    return Array

if __name__ == "__main__":
    print(select_sort([2,3,54,1,35,6,31,5,321,8,52]))