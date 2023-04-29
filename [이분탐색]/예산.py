#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
백준 예산 
이분탐색 

"""

n = int(input())
money = list(map(int,input().split()))
m = int(input())

start = 0
end = max(money)
real_money = 0 #최종 상한가

while start <= end:
    mid = (start+end)//2
    total = 0
    
    for i in money:
        if i > mid :
            total += mid
        else:
            total += i
    
    if total > m :
        end = mid-1
    else : #total<=m
        real_money = mid
        start = mid+1
print(real_money)