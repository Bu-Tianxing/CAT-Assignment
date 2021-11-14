# 二分查找

def binarySearch(Array, x):
    n = len(Array)
    if n >= 1:
        mid = (1 + (n - 1) // 2)
        if Array[mid] == x:
            return mid
        elif Array[mid] < x:
            return binarySearch(Array[mid + 1:], x)
        else:
            return binarySearch(Array[:mid], x)
    else:
        return -1

if __name__ == "__main__":
    print(binarySearch([1, 2, 3, 5, 6, 8, 31, 35, 52, 54, 321], 31))