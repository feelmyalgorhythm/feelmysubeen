#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
백준 12865 - 냅색문제

@author: kimsubin
"""

import sys
input = sys.stdin.readline


n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)] 

def knapsack(n,k,items):
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1,n+1): 
        weight, value = map(int, items[i-1])
        for j in range(1,k+1): # j = 가방에 담을 수 있는 무게 
            if weight <= j: #  물건 추가 혹은 현재 값 비교
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)
            
            else: # 못넣으니까 이전 물건까지 담았을 때의 최고 값
                dp[i][j] = dp[i-1][j]

    
    print(dp[n][k])

knapsack(n,k,items)