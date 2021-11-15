# 给定n个字符串，请对n个字符串按照字典序排列

def main():
    words = [i for i in input("请输入待排序单词").split()]
    words.sort()
    for word in words:
        print(word, end = " ")

if __name__ == "__main__":
    main()