#!/usr/bin/env python3
import string
import random


def generate_random_username():
    """
    生成随机16位字符串，作为用户名使用
    :return:
    """
    letter_range = string.ascii_letters + string.digits
    result = [random.choice(letter_range) for _ in range(16)]
    return ''.join(result)


if __name__ == '__main__':
    r = generate_random_username()
    print(r)

