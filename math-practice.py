import math
# x=float(input("Birinchi sonni kiriting: "))
# y=float(input("Ikkinchi sonni kiriting: "))
# a = x+y
# b = math.pow(y, 2)
# c = b + 2
# d = x + math.pow(x, 3) / 5
# e = math.exp(y + 2)
# c1= a / (b + math.fabs(c / d)) + e
# print(c1)

# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# c = math.pow(a, 1/5)
# d = (a + b) * b
# e = 2 * b + a * b
# f = math.pow(a, 2) + math.pow(b, 2) + 2
# t = c + math.pow(d/e, 1/4) * f
# print("%2f" % t)

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# x = float(input("To'rtinchi sonni kiriting: "))
# e = a / 4 + b / 3 + c / 2 + 1
# f = math.fabs(math.pow(x, 3) + 3 * x)
# d = math.cos(x-2)
# t = 8.2  * math.pow(x, 2)
# w1 = 0.75 + (t + math.sqrt(f + d)) / e 
# print("%.2f" % w1)

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# d = int(input("To'rtinchi sonni kiriting: "))
# x = float(input("Beshinchi sonni kiriting: "))
# e = a*math.pow(x, 2) + b*x + c
# f = x*math.pow(a, 3) + math.pow(a, 2) + math.pow(a, b-c)
# t = a*x+b
# w = c*x+d+math.pow(2, c)
# y2= (e/f) + math.cos(math.fabs(t/w))
# print("%.2f" % y2)

#  025
# a = int(input("Birinchi sonni kiriting: "))
# x = float(input("Ikkinchi sonni kiriting: "))
# b = math.sqrt(x-1) + math.sqrt(x+2)
# c = math.log10(math.sqrt(a * math.pow(x, 2)) + 2)
# d = math.sqrt(math.sqrt(x+2) + math.sqrt(x+24) + math.pow(x, 5))
# tt = (b + c) / d
# print("%.2f" % tt)

#026
# a = int(input("Birinchi sonni kiriting: "))
# x = float(input("Ikkinchi sonni kiriting: "))
# y = float(input("Uchinchi sonni kiriting: "))
# b = math.exp(x*y) - x * math.sin(a*x)
# c = (math.pow(x, 2)+ 2 ) / (math.fabs(x) + 5)
# d = math.sqrt(b-c)
# e = math.sqrt(math.log(math.pow(x,2)+2)+5)
# w2= d+e
# print("%.2f" % w2)

#020
# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# a=math.pow(x, 2)+1
# b=x*y+math.pow(y,2)
# d=a/b
# k=y+x*y
# e=math.pow(x,2) + d/k
# f=math.fabs(x*y)+5
# g=math.pow(y,2) + e/f
# j=1/math.sin(math.fabs(x))
# l=1+math.cos(x)+j
# t11=g+l
# print("%.2f" % t11)

#028
# a = int(input("Birinchi sonni kiriting: "))
# x = float(input("Ikkinchi sonni kiriting: "))
# b = x*math.sin(x/2+x/3+x/4)
# c = math.log10(math.pow(x,2)-2) + math.pow(3, a)
# d=math.cos(x+3)*math.sin(x+3)+8
# l= c/d
# bb1=b+l
# print("%.2f" % bb1)

x=float(input("Birinchi sonni kiriting: "))
y=float(input("Ikkinchi sonni kiriting: "))
a = math.pow(x, 2) + 1
b = x * y + math.pow(y, 2)
c = y + x * y
d = math.fabs(x * y) + 5
e = a / (math.pow(x, 2) + b / (math.pow(y, 2) + c / d))
f = 1 / (1+ math.cos(x) + 1 / math.sin(math.fabs(x)))
t11=e+f
print("%.2f" % t11)

a=int(input("a: "))
b=int(input("b: "))
print(a+b)