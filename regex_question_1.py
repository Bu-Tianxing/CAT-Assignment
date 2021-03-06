# NANP (North American Numbering Plan，北美编号方案)对北美地区的电话号码格式做出了定义。
# 根据这一方案，北美地区（美国、加拿大、加勒比海地区大部以及 其他几个地区）的电话号码由一个3位数的区号和一个7位数的号码构成
# （这7位数 字又分成一个3位数的局号和一个4位数的线路号，局号和线路号用连字符分隔）。
# 每位电话号码可以是任意数字，但区号和局号的第一位数字不能是0或1。
# 在书写电话号码的时候，人们往往把区号放在括号里，而且还会在区号与实际电话号码之间 加上一个连字符来分隔 。
# 匹配(555) 555-5555（右括号的后面有一个空格）、 (555)555-5555、555-555-5555中的某一个很简单，
# 但想要编写一个能够同时同时匹配这些电话号码的模式就不那么容易了。

import re

def main():
    tn = [
        "(555) 555-5555",
        "(555)555-5555",
        "555-555-5555"
    ]

    '''
    re1 = \([\d^01]\d{2}\) [\d^01]\d{2}-\d{4}
    re2 = \([\d^01]\d{2}\)[\d^01]\d{2}-\d{4}
    re3 = [\d^01]\d{2}-[\d^01]\d{2}-\d{4}
    '''
    regex = re.compile(r'\([\d^01]\d{2}\) [\d^01]\d{2}-\d{4}|\([\d^01]\d{2}\)[\d^01]\d{2}-\d{4}|[\d^01]\d{2}-[\d^01]\d{2}-\d{4}')
    for elem in tn:
        print(regex.search(elem))

if __name__ == "__main__":
    main()

# 我做的答案：[\(]?[2-9]\d{2}[\).]?[\s\-]?[2-9]\d{2}-\d{4}
# 标准答案：  [\(.]?[2-9]\d\d[\).]?[ -]?[2-9]\d\d[- ]\d{4}
# 第一个中括号里不用加.吧？后面七位 555-5555的连字符不是必加吗？怎么空格也行？
# PS：感觉是翻译的锅，这个题目有点歧义

# 反思：
# 这里我2-9我用的是\d^01，有点复杂了，主要是我不知道2-9语法上允不允许。
# 我觉得最保险正确的做法可能就是把这些用|并列起来？缝合成一个表达式可能会导致有一些不符合规定的也被匹配到，
# 如：(555 555 5555, 555) 555 5555之类的，无法控制括号要加就必须加两个，不知道具体的评分标准是什么？
# 还有一个疑问，就是这个空格为何不能直接打一个空格？\s会不会导致其他的，如制表符等空字符被匹配到？