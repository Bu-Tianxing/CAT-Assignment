# 更精确地匹配URL（URL查询字符串）

import re

def main():
    URL = [
        "http://www.forta.com/blog",
        "https://www.forta.com:80/blog/index.cfm",
        "http://www.forta.com/com",
        "http://ben:password@www.forta.com",
        "http://localhost/index.php?ab=1&c=2",
        "http://localhost:8500/"
    ]
    regex = re.compile(r"https?://(\w*:\w*@)?[-\w.]+(:[\d.]+)?(/([\w/.]*)?)?(\?\S+)?")
    for elem in URL:
         print(regex.search(elem))

if __name__ == "__main__":
    main()

# 正确答案：https?:\/\/(\w*:\w*@)?[-\w.]+(:\d+)?(\/([\w\/_.]*)?)?
# 书上的答案：https?://(\w*:\w*@)?[-\w.]+(:[\d.]+)?(/([\w/_.]*(\?\S+)?)?)?

# 反思：
# 自己写的括号的位置有点浪费算力，不过也能匹配上