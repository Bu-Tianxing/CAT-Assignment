#【题目描述】 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明:本题中，我们将空字符串定义为有效的回文串。

import re

def deleteANDlower(string):
    return re.sub("[\W_]+", "", string).lower()

def isPlalindrome(string):
    n = len(string)
    if n == 0: # 排除边界情况
        return True
    i, j = 0, n - 1 # 双指针，i指头 j指尾
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    x = input("请输入带判断的回文数：")
    print(isPlalindrome(deleteANDlower(x)))

if __name__ == "__main__":
    main()