# 美国于1963年开始使用ZIP编码（ZIP是Zone Improvement Plan的首字母缩写）。
# 美国目前有4万多个ZIP编码，它们全部由数字组成（第一位数字代表从美国东部到西部的一个地域，0代表东海岸地区，9代表西海岸地区）。
# 在1983年，美国邮政总局开始使用扩展ZIP编码，简称ZIP+4编码。新增加的4位数字对信件投递区域做了更细致的划分
# （细化到某个特定的城市街区或某幢特定的建筑物），这大大提高了信件的投送效率和准确性。
# 不过，ZIP+4编码是可选的，所以对ZIP编码进行检查通常必须同时照顾到5位数字的ZIP编码和9位数字的ZIP+4编码
# （ZIP+4编码中的后4位数字与前5位数字之间要用一个连字符隔开）。

import re
def main():
    # 第一个是“笨办法”，第二个是缝合的办法
    regex1 = re.compile(r"\d{5}-\d{4}|\d{5}")
    regex2 = re.compile(r"\d{5}(-\d{4})?")
    Adress = [
        "999 1st Avenue, Bigtown, NY, 11222",
        "132 High Street, Any City, MI, 48034-1234"
    ]
    for elem in Adress:
        print(regex1.search(elem))
        print(regex2.search(elem))

if __name__ == "__main__":
    main()

# 反思：
# 和讲的一模一样hhhhh，一遍过！