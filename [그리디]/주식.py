#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
백준 주식
그리디 문제
"""

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    result = 0
    tmp = 0
    
    for i in a:
        if tmp > i:
            result += (tmp - i)
        elif tmp < i:
            tmp = i
    print(result)