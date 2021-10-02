#30个人在一条船上，超载，需要15人下船。于是人们排成一队，排队的位置即为他们的编号。
#报数，从1开始，数到9的人下船。如此循环，直到船上仅剩15人为止，问都有哪些编号的人下船了呢？

People = list(range(1,31))
Disembark = list()
while True:
    if len(People) == 15:
        print(Disembark)
        break
    Disembark.append(People[8])
    People.pop(8)