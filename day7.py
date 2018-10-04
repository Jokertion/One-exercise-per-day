#  给定一个字典，判断该字典是否在list中存在。
#  output: True or False

_dict = {"x": "x"}
_list = [{"x": "x"}, {"y": "y"}, {"z": "z"}]

for dic in _list:
    if dic == _dict:
        print("True")
        break
else:
    print("False")
