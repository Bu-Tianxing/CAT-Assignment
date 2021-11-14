# 二分查找解决装水问题

import math

def get_r_(R, h):
    pi = math.pi
    S1 = math.acos((R - h) / R) * (R ** 2) - (R - h) * math.sqrt(R ** 2 - (R - h) ** 2) / 2
    S2 = pi * (R ** 2) / 2
    return S1/S2

def solve(R, r):
    accuracy = 10 ** (- 5)
    left, right = 0, R
    while right - left > accuracy:
        mid = (left + right) / 2
        if get_r_(R, mid) > r:
            right = mid
        else:
            left = mid
    return mid

def main():
    R = int(input("R = ?"))
    r = float(input("r = ?"))
    print(solve(R, r))

if __name__ == "__main__":
    main()