# Python 100例 练习实例12
# 题目：判断101-200之间有多少个素数，并输出所有素数。

num_list = []
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num_list.append(i)
        print("%d 为质数" % i)

print("101-200之间有【%d】个素数" % len(num_list))
