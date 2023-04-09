#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 - 귤 고르기 (lv2)

@author: kimsubin
"""

def solution(k, tangerine):
    answer = 0
    di = {}
    for i in tangerine:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    di = sorted(di.items(), key = lambda item: item[1], reverse = True)
    num = 0
    for i in range(len(di)):
        num += di[i][1]
        answer += 1
        if num >= k:
            break
    return answer
    
    