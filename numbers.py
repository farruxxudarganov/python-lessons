# Data types - Ma'lumot turlari
#1. String (matn) => "test", 'adminjon'
#2. Number (son) => integer(butun son) 5,6,0, -12; 2. float (o'nlik son) -5.85, 7.99
#3. Boolean(mantiqiy qiymat) => 1. True (haqiqat) 2. False (yolg'on)
# Integer

# a=20
# b=-30
# c=a+b
# print(c)

# Float

# pi=3.14159
# radius=10
# diametri= 2*radius
# l=2*pi*radius
# print("aylana uzunligi: ", l)

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) #5.0
# print(a*b) #6.0
# print(a**b) #8.0
# print(2*(a+b)) #10.0

# aholi_soni = 7_594_000_000 
# print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

# # Konstanta(constant) qiymatlar - o'zgarmas qiymatlar
# PI=3.14
# G=9.81

# x,y,z=7,5,-7
# print(x-z+y)

#TYPECASTING - Ma'lumot turlarini o'zgartirish
#Type checking - Ma'lumot turini tekshirish
# username="adminjon"
# age=14
# x=2.57
# is_student = True
# #type() function
# print(type(username)) # 'str'
# print(type("tester")) # 'str'
# print(type(12)) # 'int'
# print(type(age)) # 'int'
# print(type(17.87)) # 'float'
# print(type(x)) # 'float'
# print(type(False)) # 'bool'
# print(type(is_student)) # 'bool'

# firstname="Jobir"
# age=36
# massage=firstname + " " + str(age) + " yoshda"
# print(massage)

# age = 36
# print(type(age))
# age = str(age) # 36 => "36"
# print(type(age))

# print(int(121.89)) #121
# print(int(15.0)) #15
# print(float(18)) #18.0
# print(float('12.77')) #12.77

#input() va son bilan ishlash
# yosh = input("Iltimos, yoshingizni kiriting: ")
# t_yil = 2025 - int(yosh)
# print(t_yil)

# #Amaliyot

# son = int(input("istalgan son kiriting: "))
# # xabar1= f"{son} ning kvadrati {son ** 2} ga teng"
# # xabar2 = son + " ning kubi " + son**3 + " ga teng"
# xabar1 = str(son) + " ning kvadrati " + str(son**2) + " ga teng"
# xabar2 = son + " ning kubi " + son**3 + " ga teng"
# print(xabar1)
# print(xabar2)

#amaliyot 2

# yosh= int(input("Yoshingiz Nechida: "))
# yil=2025-yosh
# print(f"Siz {yil}-yilda tug'ilgansiz")

#amaliyot 3 

# a=float(input("Birinchi sonni kiriting: "))
# b=float(input("Ikkinchi sonni kiriting: "))
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")

# a=int(input("uchburchakning 1-tomonini kiriting: "))
# b=int(input("uchburchakning 2-tomonini kiriting: "))
# c=int(input("uchburchakning 3-tomonini kiriting: "))
# y_perimetri=(a+b+c)/2
# yuza = y_perimetri*(y_perimetri-a)*(y_perimetri-b)*(y_perimetri-c)**(1/2)
# print(f"Uchburchak tomonlari {a},{b},{c} bo'lsa, uning yuzi {yuza}")

# import math
# r1=int(input("1-doiraning radiusi: "))
# r2=int(input("2-doiraning radiusi: "))
# r3=int(input("3-doiraning radiusi: "))
# s1= math.pi * r1 ** 2
# s2= math.pi * r2 ** 2
# s3= math.pi * r3 ** 2
# print(f"Radiusi {r1} ga teng bo'gan doiraning yuzasi {s1} ga teng")
# print(f"Radiusi {r2} ga teng bo'gan doiraning yuzasi {s2} ga teng")
# print(f"Radiusi {r3} ga teng bo'gan doiraning yuzasi {s3} ga teng")
