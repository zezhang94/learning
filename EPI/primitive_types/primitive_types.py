import math
import random

def main():
    # bit-wise operators
    print("6 & 4 :", 6 & 4)
    print("1 | 2 :", 1 | 2)
    print("8 >> 1 :", 8 >> 1)
    print("-16 >> 2 :", -16 >> 2)
    print("1 << 10 :", 1 << 10)
    print("~0 :", ~0)
    print("15 ^ 1 :", 15 ^ 1)
    # numeric types 
    print("abs(-34.5) :", abs(-34.5))
    print("math.ceil(2.17) :", math.ceil(2.17))
    print("math.floor(3.14) :", math.floor(3.14))
    print("min(324, 12314) :", min(324, 12314))
    print("max(121, 3221) :", max(121, 3221))
    print("pow(2, 5) :", pow(2, 5))
    print("2 ** 5 :", 2 ** 5)
    print("math.sqrt(225) :", math.sqrt(225))
    # interconvert
    print("str(42) :", str(42))
    print("int('42') :", int('42'))
    print("str(3.14) :", str(3.14))
    print("float('3.14') :", float('3.14'))
    # infinity
    print("float('inf') :", float('inf'))
    print("float('-inf') :", float('-inf'))
    print("math.isclose(1.25, 1.249999999) :", math.isclose(1.25, 1.249999999))
    print("math.isclose(1.25, 1.24) :", math.isclose(1.25, 1.24))
    # random
    print("random.randrange(28) :", random.randrange(28))
    print("random.randint(8, 16) :", random.randint(8, 16))
    print("random.random() :", random.random())
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(A)
    print("random.shuffle([1, 2, 3, 4, 5, 6, 7, 8]) :", A)
    print("random.choice([1, 2, 3, 4, 5, 6, 7 ,8]) :", random.choice([1, 2, 3, 4, 5, 6, 7 ,8]))


if __name__ == '__main__':
    main()