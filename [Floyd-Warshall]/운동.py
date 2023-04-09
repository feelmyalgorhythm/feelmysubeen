#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

백준 1956 운동
플로이드와샬 유형의 문제

"""
import sys
input = sys.stdin.readline
MAX = sys.maxsize
V, E = map(int, input().split())
arr = [[MAX for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    arr[a][b] = cost

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if arr[i][j] > arr[i][k]+arr[k][j]:
                arr[i][j] = arr[i][k]+arr[k][j]

result = MAX
for i in range(1, V+1):
    result = min(result, arr[i][i])

if result == MAX:
    print('-1')
else:
    print(result)
 
