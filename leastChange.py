#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
最少交换次数
序号：#8 难度：非常难  时间限制：1000ms  内存限制：10M
描述
给出一个无序数列，每次只能交换相邻两个元素，求将原数列变成递增数列的最少交换次数。
如：数列：2,3,1，交换3和1后变成：2,1,3；交换1和2之后变成：1,2,3。总共交换2次。

输入
逗号隔开的正整数数列

输出
正整数
"""


def solution(line):
    s = line.strip().split(',')
    ans = 0
    for i in range(1, len(s)):
        for j in range(i):
            if int(s[j]) > int(s[i]):
                ans += 1
    return ans


s = "2,3,1"
print solution(s)
