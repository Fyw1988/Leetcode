# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:14:27 2022

@author: fyw
"""
s = "()()"
n = len(s)
max_len = 0
if n == 1:
    max_len = 0
if n == 2 and s[0]=='(' and s[1]==')':
    max_len =  2

str_list = [[False] * n for _ in range(n)]

for L in range(2, n+1):
    for i in range(n):
        j = i + L - 1
        if j >= n:
            break
        else:
            if L // 2 != 0:
                str_list[i][j] = False
            else: 
                if L < 3 and s[i:i+2] == "()":
                    str_list[i][j] = True
                else:
                    str_list[i][j] = str_list[i+2][j]
            if str_list[i][j] and L > max_len:
                max_len = L
