# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:10:36 2024

@author: Asus

"""
import math as m
print("1-tomon:")
a = int(input())
print("2-tomon:")
b = int(input())
print("3-tomon:")
c = int(input())
if a+b>c and a+c>b and c+b>a:
    p = (a+b+c)/2
    s = m.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Uchburchak yuzi: {s} kv.br")
else:
    print("Bunday uchburchak mavjud emas!")
