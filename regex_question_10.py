# HTML页面里的注释必须位于<!--和-->标签之间
# （这两个标签之间必须至少包含两个连字符，多于两个也没有关系）。
# 在浏览（或调试）Web页面的时候，找出所有的注释是有用的。

import re

def main():
    HTML = '''
    <!-- Start of page -->
    <HTML>
    <!-- Start of head -->
    <HEAD>
    <TITLE> My title</TITLE> <!-- Page title -->
    </HEAD>
    <!-- Body -->
    <Body>
    '''
    print(re.findall(r"(?<=<!--)(?<=-)*[\s\w]*(?=-)*(?=-->)",HTML))

if __name__ == "__main__":
    main()

# 反思：
# 直接做成思考题了，用的条件查找，原来可以要标签啊。。。
# 要标签的话应该是<!-{2,}.*?-{2,}>