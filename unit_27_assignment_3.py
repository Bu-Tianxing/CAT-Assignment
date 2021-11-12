# 插入排序

def insert_sort(Array):
    n = len(Array)
    for i in range(n):
        cur_index = i
        while cur_index != 0 and Array[cur_index - 1] > Array[cur_index]:
            Array[cur_index - 1], Array[cur_index] = Array[cur_index], Array[cur_index - 1]
            cur_index -= 1
    return Array

if __name__ == "__main__":
    print(insert_sort([2,3,54,1,35,6,31,5,321,8,52]))