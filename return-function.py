# def add_numbers(c, d):
#     return c + d
# print(add_numbers(8, 7))
# result = add_numbers(4, 6)
# print(result)

# # Qiymat qaytaruvchi funksiya
# # retinr - funksiya ichida natija qaytarish uchun ishlatiladi.
# def add_numbers(c, d):
#     return c + d
# print(add_numbers(8, 7)) # 15
# result = add_numbers(4, 6) # 10
# print(result) # 10
# def isEven(number):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"
# print(isEven(4)) # Juft
# print(isEven(7)) # Toq



# Ternary operator - shartli ifoda, qisqa if-else yozish usuli
# def isEven(number):
#     return "juft" if number % 2 == 0 else "toq"
# print(isEven(4)) # juft
# print(isEven(7)) # toq



# def toliq_ism_yasa(ism, familiya):
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism


# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")


age= int(input("Yoshingizni kiriting: "))

print("Siz endi kattasiz") if age >= 18 else print("Siz hali yoshsiz")
