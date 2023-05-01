#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

n = int(input())
li = list(map(int,input().split()))
ans = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == li[i] and ans[j] == 0:
            ans[j] = i + 1 #1부터 시작하므로 +1해줌.
            break
        elif ans[j] == 0:
            cnt += 1

print(*ans)