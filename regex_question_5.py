# 美国社会安全号码（social security number，简称SSN）由3组数字组成，
# 彼此之间以连字符分隔：第一组包含3位数字，第二组包含2位数字，第三组包含4位数字。
# 从1972年起，美国政府开始根据SSN申请人提供的住址来分配第一组里的3位数字。

import re

def main():
    SSN = ["Jone Smith: 123-45-6789"]
    regex = re.compile(r"\d{3}-\d{2}-\d{4}")
    for elem in SSN:
        print(regex.search(elem))

if __name__ == "__main__":
    main()

# 反思：
# 确实太简单了