# Python100题 练习实例5--排序
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# Input: [9, 5, 6]
# Output:[5, 6, 9]

# 冒泡排序
def _sort(num):
    for i in range(0, 2):
        for j in range(0, 2-i):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
    print(num)

_sort([6, 5, 9])

# sort方法
def _sort(num):
    num.sort()
    print(num)

_sort([6, 5, 9])
