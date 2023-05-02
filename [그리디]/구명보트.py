#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스
그리디 = 구명보트
"""

def solution(people, limit):
    number = 0
    people.sort() # 50 50 70 80
    start = 0
    end = len(people)-1
    
    while start < end:
        if people[start]+people[end] <= limit:
            start+=1
            number+=1
        end-=1
        
        
    return len(people)-number