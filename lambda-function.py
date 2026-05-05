# Lambda function - anonymous(maxfiy, nomsiz) funksiya
# syntax
# lambda argument: expression(ifoda)
# x = lambda a : a + 10
# print(x(7))

# aylana uzunligini topuvchi lambda function
# import math
# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(math.pi, 5))

# product = lambda x, y : x ** y
# print(product(5, 4))

# def daraja(n):
#     return lambda x : x ** n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(kvadrat(5)) #5 ** 2 = 25
# print(kub(33)) # 33 * 3= 35937

# map function
# from math import sqrt
# sonlar = list(range(11)) # 0 dan 10 gacha sonlar
# map(sqrt , sonlar)
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)
numbers = list(map(int, input().split()))
print(numbers)
#  0 1 5 8 12 -5
# print("Hello World".split())
# print("0 1 5 8 12 -5".split())