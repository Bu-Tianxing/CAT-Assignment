# 输入两个正整数m和n，设计函数求其最大公约数和最小公倍数。

def gcd(m,n):
    while True:
        for i in range(min(m,n),0,-1):
            if m % i == 0 and n % i == 0:
                return i

def lcm(m,n):
    while True:
        for i in range(min(m,n),m*n+1):
            if i % m == 0 and i % n == 0:
                return i

# 反思：
# 看了讲解有点懵，这个递归的思想感觉就是在最后调用自己来实现循环，直到算出需要的答案。
# 最大公约数和最小公倍数的性质掌握的不是太好，我还是用暴力破解的方法挨个计算，可能这样会导致算大数的时候慢一些。
# 感觉到了main的作用，用户需要输入的时候可以把input放到main底下