# 输出[1-2001)范围内素数
def prime_number(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
            break
    return n

Result = list()
for i in range(1,2001):
    res = prime_number(i)
    if res != 0:
        Result.append(res)
print(Result)