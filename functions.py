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

# default vaulue 
# def yosh_hisobla(ism = "Olim", tugilgan_yil = 1980):
#     yosh = 2026 - tugilgan_yil
#     print(f"{ism}ning yoshi: {yosh}")

# yosh_hisobla("Ismoil", 2000) # Ismoilning yoshi: 26
# yosh_hisobla("Gulbahor", 1995) # Gulbahorning yoshi: 31
# yosh_hisobla() # Olimning yoshi: 46
# yosh_hisobla("Jumagul", 1960) # Jumagulning yoshi: 66
# yosh_hisobla()

def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh_hisobla(tyil)
