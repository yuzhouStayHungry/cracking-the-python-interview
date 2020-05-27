# -*- coding: utf-8 -*-
# @Time      : 2020-04-17 14:32
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : huaweibishi.py
# @Software  : PyCharm

# line = int(input())
# dic = {}
# for i in range(line):
#     key, val = input().split()
#     key = int(key)
#     val = int(val)
#     if key in dic:
#         dic[key] += val
#     else:
#         dic[key] = val
# for i in sorted(dic.keys()):
#     print(str(i)+" "+str(dic[i]))
#

# sentence = input()
# word = sentence.split(' ')
# for w in reversed(word):
#     print(w, end=' ')

# line = int(input())
# s = []
# for i in range(line):
#     s.append(input())
#
# for word in sorted(s):
#     print(word)
#

# num = int(input())
# num2bin = bin(num)
# count = 0
# print(list(num2bin)[2:])
# for i in list(num2bin)[2:]:
#     if i == '1':
#         count +=1
# print(count)

# num = int(input())
# count = 0
# while num:
#     count += 1
#     num = num & (num-1)
# print(count)

# n = num & (num-1)
# print(n)

# nums = int(input())
# count = 0
# sum_num = 0
# for i in range(nums):
#     num = int(input())
#     if num < 0:
#         count += 1
#     else:
#         sum_num += num
#         avg = round(sum_num / (nums - count),1)
# print(count, avg)

nums = int(input())
a = []
for i in range(nums):
    a.append(input())
fu = []
zheng = []
for j in a:
    if int(j) < 0:
        fu.append(int(j))
    else:
        zheng.append(int(j))
print(len(fu), round(sum(zheng) / len(zheng), 1))
