# 判断用户输入的数字是否为质数

# method_1
# y = int(input('请输入一个正整数: '))
# x = y // 2
# while x > 1:
#     if y % x == 0:
#         print(y, 'has factor', x)
#         break
#     x -= 1
# else:
#     print(y, 'is prime')

# method_2
y = int(input('请输入一个正整数: '))
if y > 1:
    for i in range(2, y):
        if y % i == 0:
            print(y, '不是质数')
            print(y, '有因数', i)
            break
    else:
        print(y, '是质数')
else:
    print(y, '不是质数')
