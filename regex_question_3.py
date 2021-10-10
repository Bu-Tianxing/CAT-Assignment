# 加拿大邮政编码由6个交替出现的字母和数字组成。每个编码字符分成两部分：
# 前3 个字符给出了FSA（forward sortation area，转发分拣代码）代码，
# 后3个字符给出了LDU（local delivery unit，本地投递单位）代码。
# FSA代码的第一个字符用来 表明省、市或地区（这个字符有18种有效的选择，
# 比如A代表纽芬兰地区，B代表 新斯科舍地区，K、L、N和P代表安大略省，M代表多伦多市，等等），
# 模式应该对 此作出验证，确保这个字符的有效性。在书写加拿大邮政编码的时候，FSA代码和LDU代码之间通常要用一个空格隔开。

import re

def main():
    Adress = [
        "123 4th Street, Toronto, Ontario, M1A 1A1",
        "567 8th Avenue, Montreal, Quebec, H9Z 9Z9"
    ]
    regex1 = re.compile(r"[A-R]\d[A-Z]\s\d[A-Z]\d")
    regex2 = re.compile(r"[A-R](\d[A-Z])\s\1\d")
    for elem in Adress:
        print(regex1.search(elem))
        print(regex2.search(elem))

if __name__ == "__main__":
    main()

# [ABCEGHJKLMNPRSTVXY]\d[A-Z] \d[A-Z]\d

# 反思：
# 因为觉得正常的表达式过于简单了
# 所以使用了回溯引用简化表达式，想得满分哈哈哈哈
# 那个18个字母是真的没在题干里给出，有毒