#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
백준 1655 - 우선순위 큐 heapq
- 숫자를 하나씩 받고 지금까지의 숫자들 중에서 비교하며 중앙 찾기

@author: kimsubin
"""

import sys
import heapq
input = sys.stdin.readline

cnt = int(input())
left, right = [], [] 
# 숫자를 하나씩 받고 지금까지의 숫자들 중에서 비교하며 중앙 찾기
for i in range(cnt):
  num = int(input())
  
  if len(left) == len(right):
    heapq.heappush(left, (-num, num))
  else:
    heapq.heappush(right, (num, num))

  if i > 0 and left[0][1] > right[0][1]:
    left_l = heapq.heappop(left)[1] #중간값보다 작은 것을 left 
    right_l = heapq.heappop(right)[1] #중간값보다 큰 것을 right
    heapq.heappush(left, (-right_l, right_l))
    heapq.heappush(right, (left_l, left_l)) 

  print(left[0][1])