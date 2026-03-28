# Function - Ma'lum bir vazifani bajaruvchi kod bloklari. 
# Ular bir marta yozilib, bir necha marta chaqirilishi mumkin.
# print(), range(), input(), list(), type()
# declaratsiya - funksiya nomi va uning bajaradigan vazifasini aniqlash
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# # call - funksiyani chaqirish
# salom_ber()  # Funksiyani chaqirish
# salom_ber()  # Funksiyani yana bir marta chaqirish
# print("hey guys")
# range(1, 10, 2)

# # FUNKSIYANI qiymatga uzatish 
# # parametrlar - funksiyaga uzatiladigan qiymatlar
# # parametr
# # argument 
# def salom_ber(ism):
#     """Foydalanuvchining ismini qabul qilib, salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, {ism}!")
# salom_ber("Ali")  # "Ali" qiymatini funksiyaga uzatish
# salom_ber("Vali")  # "Vali" qiymatini funksiyaga uzatish
# def yigindi(a, b):
#     print(a + b)

# yigindi(5, 10)
# yigindi(3, 7)

def yosh_hisobla(ism, tugilgan_yil):
    yosh = 2026 - tugilgan_yil
    print(f"{ism}ning yoshi: {yosh}")

yosh_hisobla("Ismoil", 2000) # Ismoilning yoshi: 26
yosh_hisobla("Gulbahor", 1995) # Gulbahorning yoshi: 31
