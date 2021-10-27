# 题目：字符串反转
# 题目描述：编写程序，使用两种方法实现字符串整体翻转，但是里面每一个单词的顺序不翻转。
# （提示：两种方法可以分别使用库函数和不用库函数来实现）
# 输入格式：输入在一行中给出需要反转的字符串。
# 输出格式：输出反转完成后的字符串
# 输入样例： i am a student
# 输出样例： tneduts a ma i

def main():
    ls = list(input("请输入一句话"))
    ls.reverse()
    return "".join(i for i in ls)

if __name__ == "__main__":
    print(main())

# 反思：
# list()除了用来创建空列表，还可以list(string)来将字符串里的每个东西都存入列表（包括空格）