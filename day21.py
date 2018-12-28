# Python 练习实例19
# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
from functools import reduce


def factor():
    for n in range(1, 1000):
        a = [i for i in range(1, n) if n % i == 0]  # 找n的因数
        if len(a) > 1:
            sum = sum(a)
            # sum = reduce(lambda x, y: x + y, a)  # 求和
            if sum == n:
                print(a, n)


factor()


"""
output:
[1, 2, 3] 6
[1, 2, 4, 7, 14] 28
[1, 2, 4, 8, 16, 31, 62, 124, 248] 496
"""
