#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

[구현,수학] , 팩토리얼 or permutations
permutations 풀이로는 효율성에서 걸림.. -> 팩토리얼로 풀이
팩토리얼 규칙 찾기까지 어려웠음..

@author: kimsubin
"""

import math

def solution(n, k):
    answer = [i for i in range(1, n + 1)]
    result = []
    k = k-1

    while answer:
        # k / (n-1)! - 몫
        num = k // math.factorial(n - 1)
        result.append(answer[num])
        del answer[num]

        k = k % math.factorial(n - 1) #k다시
        n -= 1

    return result

