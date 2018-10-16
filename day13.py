# Python 100例 练习实例17
# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input('请输入字符: ')
letters = 0
spaces = 0
numbers = 0
others = 0
for a in s:
    if a.isalpha():
        letters += 1
    elif a.isspace():
        spaces += 1
    elif a.isnumeric():
        numbers += 1
    else:
        others += 1
print('letters:{}, spaces:{}, numbers:{}, others:{}'.format
      (letters, spaces, numbers, others))
