# JavaScript（以及包括ActionScript和ECMAScript变体在内的其他脚本语言）
# 代码里的注释均以//开头。正如上一个例子中所示，找出给定页面里的所有注释还是挺实用的。

import re

def main():
    JavaScript = '''
    <SCRIPT LANGUAGE="JavaScript">
    // Turn off fields used only by replace
    fuction hideReplaceFields() {
        document.getElementByID('RegExReplace').disabled=true;
        document.getElementByID('replaceheader').disabled=true;
    }
    // Turn on fields used only by replace
    function showReplaceFields() {
        document.getElementByID('RegExReplace').disabled=false;
        document.getElementByID('replaceheader').disabled=false;
    }
    '''
    print(re.findall(r"//.*",JavaScript))

if __name__ == "__main__":
    main()

# 反思：
# 有点担心跨行匹配到下面去了，后来发现不会跨行匹配，还是很简单的