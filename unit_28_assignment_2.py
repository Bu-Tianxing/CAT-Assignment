# 归并排序

def merge(left, right):
    i, j = 0, 0
    result = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(Array):
    if len(Array) <= 1:
        return Array
    mid = len(Array) // 2 # slice操作需要整数型
    left = mergeSort(Array[:mid])
    right = mergeSort(Array[mid:])
    return merge(left, right)

if __name__ == "__main__":
    print(mergeSort([2,3,54,1,35,6,31,5,321,8,52]))