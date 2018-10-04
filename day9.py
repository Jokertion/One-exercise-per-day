# __doc__ = "问题：给定一个数组，" \
"其中该数组中的每个元素都为字符串，" \
"删除该数组中的空白字符串。"
# 要求： 不创建新的list，只对当前list进行处理。

_list = ["A", "", "", "B", "", "C", "", "", "D", "", ' ']

# method_1
while '' in _list:
    _list.remove('')
print("method_1", _list)

# method_2
# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素
_list = ["A", "", "", "B", "", "C", "", "", "D", "", ' ']


def not_empty(s):
    return s and s.strip()


res = filter(not_empty, _list)
print("method_2", list(res))
