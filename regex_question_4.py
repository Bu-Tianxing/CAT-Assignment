# 英国邮政编码由5-7个字母和数字构成，这些编码是由英国皇家邮政局（royal mail）定义的。
# 英国邮政编码分成两部分：外部邮政编码[或称外码（outcode）]
# 和内部邮政编码[或称内码（incode）]。外码是一到两个字母后面跟着一到两位数字，
# 或者一到两个字母后面跟着一个数字和一个字母。内码永远是一位数字后面跟着两个字母
# （除C、I、K、M、O和V以外的任意字母，这6个字母不会在邮政编码中出现）。内码和外码之间要用一个空格隔开。

import re

def main():
    Adress = [
        "171 Kyverdale Road, London N16 6PS",
        "33 Main Street, Portsmouth, P01 3AX",
        "18 High Street, London NW11 8AB"
    ]
    regex1 = re.compile(r"[A-Z^CIKMOV]{1,2}\d(\d|[A-Z^CIKMOV])?\s\d[A-Z^CIKMOV]{2}")
    regex2 = re.compile(r"([A-Z^CIKMOV]){1,2}\d(\d|\1)?\s\d\1{2}")
    for elem in Adress:
        print(regex1.search(elem))
        print(regex2.search(elem))

if __name__ == "__main__":
    main()

# 反思：
# 题目有歧义啊，我以为是内外码都要排除那几个字母。
# 第二个使用回溯引用的时候不知道为什么失灵了，匹配不出来，不过反正前面不要排除，直接A-Z就行了，以后还是尽量写笨办法。