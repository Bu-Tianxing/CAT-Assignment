# 正则表达式常用于验证电子邮件地址，不过，即使是一个简单的电子邮件地址，验证起来也绝非易事。

import re

def main():
    E_mail = "My name is Ben Forta, and my email address is ben@forta.com"
    regex = re.compile(r"\w[\w.]*@[\w.]+[A-Za-z]+")
    print(regex.search(E_mail))

if __name__ == "__main__":
    main()

# 正确答案：(\w+\.)*\w+@(\w+\.)+[A-Za-z]+
# 反思：我写的可能会导致 xxx.@xxx.com 也被匹配到，背正确答案吧还是