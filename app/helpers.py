#!/usr/bin/env python3
import os
from hashlib import md5
import string
import random


def generate_random_username():

    letter_range = string.ascii_letters + string.digits
    result = [random.choice(letter_range) for _ in range(16)]
    return ''.join(result)


# def calculate_md5_for_file(file):
#
#     stat_info = os.stat(file)
#     if int(stat_info.st_size) / (1024 * 1024) >= 1000:
#         return calculate_md5_for_bigfile(file)
#     m = md5()
#     m.update(file.read())
#     return m.hexdigest()


def calculate_md5_for_bigfile(file):

    m = md5()
    buffer = 8192  # why is 8192 | 8192 is fast than 2048
    while 1:
        chunk = file.read(buffer)
        if not chunk:
            break
        m.update(chunk)
    file.seek(0, 0)
    return m.hexdigest()


# def calMD5ForFolder(dir, MD5File):
#     outfile = open(MD5File, 'w')
#     for root, subdirs, files in os.walk(dir):
#         for file in files:
#             filefullpath = os.path.join(root, file)
#             """print filefullpath"""
#
#             filerelpath = os.path.relpath(filefullpath, dir)
#             md5 = calMD5ForFile(filefullpath)
#             outfile.write(filerelpath + ' ' + md5 + "\n")
#     outfile.close()


def get_file_info(file_path):

    pass


if __name__ == '__main__':
    r = generate_random_username()
    print(r)

