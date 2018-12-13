# __doc__ = "问题： 给定一个字典，删除其中的为None的键值对，结果为字典。"
# 要求：用字典推导式实现，输出仍然为dict

_dict = {
    "cname": "百度",
    "st_code": None,
    "salary": 0,
    "python": "要求"
}

print({k[0]: k[1] for k in _dict.items() if k[1] is not None})

