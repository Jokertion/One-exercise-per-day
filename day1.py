"问题： 给定一个字典，对字典中的key，value互换。"
# 要求： 一行代码实现（字典推导式实现）
# output: {"v1": "k1", "v2": "k2", "v3": "k3", "v4": "k4"}

_dict = {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4"}


print({v:k for k,v in _dict.items()})
