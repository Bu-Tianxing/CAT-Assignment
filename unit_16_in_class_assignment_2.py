# 题目描述：给出一个字符串和多行文字，在这些文字中找到字符串出现的那些行。 你的程序还需支 持大小写敏感选项：当选项打开时，表示同一个字母的大 写和小写看作不同的字符；当选项关闭时， 表示同一个字母的大写和小写看作相同的字符。
# 输入格式：输入的第一行包含一个字符串S，由大小写英文字母组成。
# 第二行包含一个数字，表示大小写敏感的选项，当数字为0时表示大小写不敏感，当数字为1时表示大小写敏感。
# 第三行包含一个整数 n，表示给出的文字的行数。
# 接下来n行，每行包含一个字符串，字符串由大小写英文字母组成，不含空格和其他字符。

def main():
    string_ = input("要匹配啥？")
    sensitive_ = int(input("大小写敏感：0不敏感 1敏感"))
    n = int(input("要匹配几个玩意儿？"))
    text = []
    for i in range(n):
        text.append(input("输入要匹配的玩意儿？"))
    if not sensitive_:
        string_.lower()
        for i in text:
            i.lower()
    for j in range(n):
        if string_ in text[j]:
            print(text[j])
    return 0

if __name__ == "__main__":
    main()

# 反思：
# 用了列表存放所有的输入，答案里好像是输入一个判断一个，这样可以少写一个循环。