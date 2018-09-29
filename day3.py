# Python100题 练习实例4--判断第几天
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# Input 2018 9 18
# Output 220

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def date_account(date):
    y, m, d = date.split()
    y, m, d = int(y), int(m), int(d)
    print("y =", y, "m =", m, "d =", d)
    
    # 判断闰年否
    if y % 4 == 0:
        month[1] = 29
        
    # 计算本月之前的总天数
    num = 0
    for i in month[0:m-1]:
        # print('遍历到的i', i)
        num += i
        
    # 加上本月的天数 计算总天数
    all_num = d + num
    print('it is the %dth day' % all_num)
    
    
date_account('2020 1 19')
