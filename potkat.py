# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 06:55:27 2019

@author: Accel
"""

n=int(input("num: "))
x=0

for i in range(1,n+1):
    num=int(input())
    x+=((num//10)**(num%10))
print(x)
