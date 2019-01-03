# Python 练习实例27
# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

def recursive(str):
    if str == '':
        return str
    return recursive(str[1:]) + str[0]

