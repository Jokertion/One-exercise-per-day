# Python 100例  练习实例18
# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 程序分析：关键是计算出每一项的值。

from functools import reduce

n = input("请输入几个数相加：")
a = input("请输入初始值a：")
if n.isnumeric() and a.isnumeric():
    n = int(n)
    a = int(a)
else:
    print('请输入整数')

tn = 0
alist = []
for i in range(n):
    tn = tn + a
    a = a * 10
    alist.append(tn)
    print(tn)

add = reduce(lambda x, y: x + y, alist)
print('结果和为: %d' % add)
