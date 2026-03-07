# Tarmoqlanish Operatori. If - agar, else - aks holda
# age = int(input("Yoshingizni kiriting: "))
# if age < 18 : 
#     print("Siz hali yoshsiz, kirishga ruxsat yoq")
# else:
#     print("Sizga kirishga ruxsat bor")

# ball = int(input("Imtihondan olgan ballingizni kiriting: "))
# if ball < 56:
#     print("Siz imtihondan o'ta olmadingiz")
# else:
#     print("Siz imtihondan o'ta oldingiz")

# age = int(input("Yoshingizni kiriting: "))
# if age < 16:
#     print("Siz passport ololmaysiz.")
# else:
#     print("Siz passport olishingiz mumkin.")

# Amaliyot

# 1-mashq
# son = int(input("Hohlagan sonni kiriting: "))
# if son > 0:
#      print("Musbat son")
# elif son == 0:
#      print("Musbat ham emas, manfiy son ham emas")
# else:
#      print("Manfiy son")

# 2-mashq
# son = int(input("Hohlagan sonni kiriting: "))
# if son % 2 == 0:
#     print("Juft son")
# else:
#     print("Toq son")

# 3-mashq
# son = int(input("Hohlagan sonni kiriting: "))
# if son % 5 == 0:
#     print("Bu son 5 ga bo'linadi")
# else:
#     print("Bu son 5 ga bo'linmaydi")

# 4-mashq
# son = int(input("Hohlagan sonni kiriting: "))
# if son % (2 and 3) == 0:
#     print("Bu son 6 ga bo'linadi")
# else:
#     print("Bu son 6 ga bo'linmaydi")

# 5-mashq
# a=int(input("Birinchi tomini kiriting: "))
# b=int(input("Ikkinchi tomonini kiriting: "))
# c=int(input("Uchinchi tomonini kiriting: "))
# if a + b > c and b + c > a and a + c > b :
#     print("Uchburchak bo'la oladi")
# else: 
#     print("Uchburchak bo'la olmaydi")

# 6-mashq
# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# if a > b:
#     print(a)
# else:
#     print(a, b)

# 7-mashq
# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# if a <= b :
#     a = 0
#     print(a, b)
# else:
#     print(a, b)

# 8-mashq
# import math
# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# c=int(input("3-sonni kiriting: "))
# if a>=b>=c:
#     print(2*a, 2*b, 2*c)
# else:
#    print(int(math.fabs(a)), int(math.fabs(b)), int(math.fabs(c)))

# 9-mashq
# x=int(input("1-sonni kiriting: "))
# y=int(input("2-sonni kiriting: "))
# a=2 * x * 2 * y
# b=(x + y) / 2
# if x > y:
#     x = a
#     y = b 
# else:
#     y = a 
#     x = b

# print(x, y)

# 10-mashq
# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# c=int(input("3-sonni kiriting: "))
# if a<b<c:
#     print("YES")
# else:
#     print("NO")

# x=float(input("1-sonni kiriting: "))
# y=float(input("2-sonni kiriting: "))
# print(max(x, y), min(x, y))

# x=int(input("Birimchi sonni kiriting: "))
# y=int(input("Ikkinchi kiriting: "))
# z=int(input("Uchunchi kiriting: "))
# print(max(x+y+z, x, y, z), (min(x+y/2, x, y,z)**2))

# import math
# x=float(input("Birinchi sonni kiriting: "))
# y=float(input("Ikkinchi sonni kiriting: "))
# if x<0 and y<0:
#     print(abs(x, y))
# elif x<0 or y<0:
#     print(x+0.5 , y+0.5)
# elif x>0 and y>0:
#     print(x,y)

# import math
# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# c=int(input("3-sonni kiriting: "))
# D=b**2-4*a*c
# if D>0:
#     x1 = (- b + math.sqrt(D)) / 2 (2 *a)
#     x2 = (- b - math.sqrt(D)) / 2 (2 *a)
#     print("%.2f" % x1, "%.2f" % x2)
# elif D == 0:
#     x = -b / (2 * a)
#     print("%2f" % x)
# else:
#     print("NO")

# x=int(input("Birimchi sonni kiriting: "))
# y=int(input("Ikkinchi sonni kiriting: "))
# z=int(input("Uchunchi sonni kiriting: "))
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z= z ** 2

# print(x, y, z)

# c
# c
# c

# if 1 <= x <= 3:
#     print(x)
# if 1 <= y <= 3:
#     print(y)
# if 1 <= z <= 3:
#     print(z)

# a=float(input("Birinchi sonni kiriting: "))
# b=float(input("Ikkinchi sonni kiriting: "))
# c=float(input("Uchinchi sonni kiriting: "))
# d=float(input("To'rtinchi sonni kiritng"))
# max_value = max(a, b, c, d)
# min_value = min(a, b, c, d)
# if a <= b<= c <= d :
#      a = b = c = d = max_value  
# else:
#      a = b = c = d = min_value  
# print(a, b, c, d)


# x=float(input("1-sonni kiriting: "))
# y=float(input("2-sonni kiritng: "))
# g = (x+y) /2
# h = 2*x*y
# if x<y:
#     x=g
#     y=h
# elif x>y:
#     x=h
#     y=g
# print(x, y)


# x=float(input("Birinchi sonni kiriting: "))
# y=float(input("Ikkinchi sonni kiriting: "))
# z=float(input("Uchinchi sonni kiriting: "))
# min_value=min(x,y,z)
# if x<1 and y<1 and z<1:
#     if min_value==x:
#        x=(y+z)/2
#     elif min_value==y:
#        y=(x+z)/2
#     else:
#        z=(x+y)/2

# print(x,y,z)

