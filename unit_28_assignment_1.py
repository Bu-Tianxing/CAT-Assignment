# 快速排序

def partition(Array, start, end):
    i = start - 1
    pivot = Array[end]
    for j in range(start, end):
        if Array[j] <= pivot:
            i += 1
            Array[i], Array[j] = Array[j], Array[i]
    Array[i+1], Array[end] = Array[end], Array[i+1]
    return i + 1

def quickSort(Array, start, end):
    if start < end:
        pi = partition(Array, start, end)
        quickSort(Array, start, pi - 1)
        quickSort(Array, pi + 1, end)
    return Array

if __name__ == "__main__":
    print(quickSort([2,3,54,1,35,6,31,5,321,8,52], 0, 10))