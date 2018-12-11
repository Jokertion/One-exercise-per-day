# __doc = "问题： 给定两个list，对list中的每个位置的数据进行合并，只保留和为3的倍数的数据。"
# 要求： **最好**用一行代码实现。
list_a = [1, 2, 3, 4, 5]
list_b = [2, 3, 4, 6, 10]
# output = [3, 15]

print([i + j for i, j in zip(list_a, list_b) if (i + j) % 3 == 0])
