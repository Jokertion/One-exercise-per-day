# Python 练习实例14
# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def div_prime(num):
    # 判断是否为质数
    if is_prime(num):
        print('{0}=1*{0}'.format(num, num))
        return

    # 收集质因数
    print('%d=' % num, end='')
    li = []
    while num != 1:
        if is_prime(num):
            li.append(num)
            break
        for index in range(2, num + 1):
            if num % index == 0:
                li.append(index)
                num //= index
                break
    # 打印
    for i in li[:-1]:
        print('{0}*'.format(i), end='')
    print(li[-1])


div_prime(1200)
