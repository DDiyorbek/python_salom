import math as m
print("1-koeffitsiyent:")
a = int(input())
print("2-koeffitsiyent:")
b = int(input())
print("3-koeffitsiyent:")
c = int(input())
d = b**2 - 4*a*c
if d>0:
    x1 = (-b+m.sqrt(d))/(2*a)
    x2 = (-b-m.sqrt(d))/(2*a)
    print(f"x1 = {x1} ; x2 = {x2}")
elif d==0:
    x = (-b)/(2*a)
    print(f"x = {x}")
else:
    print("Tenglama yechimga ega emas ekan!")