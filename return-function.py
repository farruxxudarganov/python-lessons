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

def juft_toq(son):
    if son % 2 == 0:
        return f"{son} - juft son"
    else:
        return f"{son} - toq son"
son = int(input("Son kiriting: "))
print(juft_toq(son))