#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
백준 - 이항계수 :  페르소나 정리

@author: kimsubin
"""

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
p = 1000000007

def factorial(N):
    n = 1
    for i in range(2,N+1):
        n = (n*i)%p
        
    return n
def answer(n,k):
    if k==0:
        return 1
    elif k==1:
        return n
    num = answer(n,k//2)
    if k%2:
        return num*num*n%p
    else:
        return num*num%p
x = factorial(N)
y = factorial(N-K) * factorial(K)%p

print(x*answer(y,p-2)%p)