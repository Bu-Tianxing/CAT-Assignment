# 输出九九乘法表（每行有1/2/3/4/5/6/7/8/9个等式）

def main():
    for i in range(1,10):
        for j in range(1,10):
            if i >= j:
                print("%d*%d=%d"%(i,j,i*j), end = " ")
        print()

if __name__ == "__main__":
    main()