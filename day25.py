# Python 练习实例26
# 题目：利用递归方法求5!。

def factorial_num(n):
    sum = 0
    if n == 1:
        return 1
    if n > 1:
        sum = n * factorial_num(n - 1)  # 每次要执行的操作
    return sum


print(factorial_num(5))
