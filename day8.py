# 问题：在dict中所有的内置方法中，
# 剔除所有以双下划线开头的方法，输出结果为列表形式
# 要求： 最好一行代码实现。
# 已知：dir(dict) 获取字典的所有内置方法

print(dir(dict))
print([i for i in dir(dict) if not i.startswith('__')])
