# 实现查找某个字符在字符串中出现次数

def main():
    string = input("请输入待查找字符串")
    x = input("请输入需要查找的字符")
    return string.count(x)

if __name__ == "__main__":
    print(main())