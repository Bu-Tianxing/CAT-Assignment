# 【题目描述】 A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自 找地方睡觉。日上三杆，
# A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己 的一份。
# B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。
# C、D、E 依次醒来，也按同样的方法拿鱼。
# 问他们台伙至少捕了多少条鱼?以及每个人醒来时见到了多少鱼？

def solve():
    fish, flag = 1, True
    while True:
        total = fish
        for i in range(5): # 判断五次
            if total % 5 == 1: # 若满足，再判断一次
                total = (total - 1) // 5 * 4
                flag = True
            else: # 若不满足，换个数继续试
                flag = False
                fish += 1
                break # 跳出for循环，因flag限制，会再次进去while循环里的for循环
        if flag: # 当且仅当满足提议的时候才跳出while循环
            break
    return fish

if __name__ == "__main__":
    print(solve())