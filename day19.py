# __doc__ = "问题： 给定一个数字1234567890，输出它的二进制表示形式，以字符串形式输出。"
# 要求： 禁止使用内置方法实现。
num = 1234567890

binary = ''
while num > 0:
    b_num = num % 2
    binary = str(b_num) + binary
    num = num // 2
print(binary)
