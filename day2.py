# Python100题 练习实例1--循环嵌套
# 题目：有四个数字：1、2、3、4，
# 能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4,
# 组成所有的排列后再去 掉不满足条件的排列。
num = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)
                num += 1
print(num)
print('*'*100)
# 变形：输出三位数可重复的数字
num = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            print(i, j, k)
            num += 1
print(num)
