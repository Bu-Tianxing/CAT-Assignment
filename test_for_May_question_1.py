#A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。
#日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。
#B第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份
#C、D、E依次醒来，也按同样的方法拿鱼。问他们至少捕了多少条鱼?

def distribution(n):
    if n % 5 == 1:
        return n//5*4
    else:
        return 0

for i in range(1,10000):
    result = i
    A = distribution(i)
    if A != 0:
        B = distribution(A)
        if B != 0:
            C = distribution(B)
            if C != 0:
                D = distribution(C)
                if D != 0:
                    E = distribution(D)
                    if E !=0:
                        print("他们至少捕了", result, "条鱼。")

# 反思：
# 和答案相比，没有把判断过程做到程序化，如果是一百个人分鱼，那就麻烦了。