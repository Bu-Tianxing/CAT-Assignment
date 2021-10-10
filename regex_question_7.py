# 匹配URL是一件相当有难度的任务，其复杂性取决于你想获得多么精确的匹配结果。
# URL匹配模式至少应该匹配到协议（http或https）、主机名、可选的端口号和路径。

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
    regex = re.compile(r"https?://[-\w.]+(/\d+)?(/([\w.]*)?)?")
    for elem in URL:
         print(regex.search(elem))

if __name__ == "__main__":
    main()

# 正确答案：https?:\/\/[-\w.]+(:\d+)?(\/([\w\/_.]*)?)?
# 小蓝书上是：https?://[-\w.]+(:\d+)?(/([\w/_.]*)?)?
# 好像/不用转义，还有最后的路径里的\w是不是已经包括了下划线_？

# 反思：
# 有点不知道这些主机名、主机名、可选的端口号和路径的格式是什么