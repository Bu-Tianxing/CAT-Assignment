# IP地址由4个字节构成（这4个字节的取值范围）。IP地址通常被写成以4组以.字符分隔的整数（每个整数由1~3位数字构成）。

import re

def main():
    IP = ["Localhost is 127.0.0.1"]
    regex = re.compile(r"(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))")
    for elem in IP:
        print(regex.search(elem))

if __name__ == "__main__":
    main()

# 反思：
# 注意括号要加全，4种情况|并列要有一层，一整个（| | | |）要第二层，加了\.要第三层，(连着忘了三次。。。debug了三次）
# 另外，\.需要转义（这个我也忘了，总共debug了四次）