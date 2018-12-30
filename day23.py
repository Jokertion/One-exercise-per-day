# Python 练习实例13
# 题目：打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
def flower_num():
    f_num = []
    for num in range(100, 1000):
        a, b, c = str(num)[0:3]
        if num == int(a) ** 3 + int(b) ** 3 + int(c) ** 3:
            f_num.append(num)
    print(f_num)
