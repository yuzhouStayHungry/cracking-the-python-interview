# -*- coding: utf-8 -*-
# @Time      : 2020-04-20 22:10
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : string_repeat.py
# @Software  : PyCharm

'''
题目描述：
找出一个字符串中出现次数最多的字符，如果有多个出现次数相同的字符，那就找出最先出现的那个字符
'''

from collections import defaultdict


def most_common(s):
    dic = defaultdict()
    count_str = 0
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
    dic_sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic_sort)
    print(dic_sort[0][0])


most_common('absdsdb')

# import string
#
# str_c = "dasdasdasds"
# str_letter = string.ascii_letters
# dict_letter = {}
# for letter in str_letter:
#     dict_letter[letter] = []
# for i in str_c:
#     dict_letter[i].append(i)
# for count in str_letter:
#     if len(dict_letter[count]) != 0:
#         print("%s的个数为%d" % (count, len(dict_letter[count])))
#
#
# from collections import Counter
#
#
# def get_max_char(s):
#     s = 'abcdacdgjkdka'
#     count = Counter(s)
#     count_list = list(count.values())
#     max_value = max(count_list)
#     max_list = []
#     for k, v in count.items():
#         if v == max_value:
#             max_list = max_list.append(k)
#         max_list = sorted(max_list)  # 加这个排序的原因是，如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母
#     return max_list[0]

from collections import Counter


def ordered_letters(s, n=3):
    c = Counter(s.replace(' ', ''))
    top_n = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))[:n]
    for i, t in enumerate(top_n):
        c, f = t
        if i == 0:
            print('1st most frequent', c + '.', 'Appearances:', f)
        elif i == 1:
            print('2nd most frequent', c + '.', 'Appearances:', f)
        elif i == 2:
            print('3rd most frequent', c + '.', 'Appearances:', f)
        else:
            print(str(i + 1) + 'th most frequent', c + '.', 'Appearances', f)


sent = "china construction bank"
ordered_letters(sent, 5)

# from collections import Counter
#
# ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
#
# def ordered_letters(s, n=3):
#     ctr = Counter(c for c in s if c.isalpha())
#     ctr = sorted(ctr.items(), key=lambda x: (-x[1], x[0]))[:n]
#     for index,value in enumerate(ctr):
#         print "{:s} most frequent: '{:}'. Appearances: {:}".format(ordinal(index+1),value[0],value[1])
#
# s = "achina aconstruction banck"
# ordered_letters(s, n=3)
