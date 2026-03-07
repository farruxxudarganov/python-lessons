# # String methods
# ism = "James"
# familiya = "Lebron"
# ism_sharif= f"{ism} {familiya}"
# # upper() va lower() 
# print(ism_sharif.upper())
# print("Adminjon".upper())
# print(ism_sharif.lower())
# print("Admin Janoblari".lower())
# ism_sharif = ism_sharif.upper()
# print(ism_sharif) #ism_sharif
# # title() va capitalize()
# print("donald trump".title())
# print(ism_sharif.title())
# print('vladimir putin'.capitalize())
# print(ism_sharif.capitalize())
# #strip(), rstrip() va lstrip()
# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# input()
# username1 = input("Iltimos, GitHub username kiriting: ")
# print(f"Sizning GitHub username: {username1}")

# firstname = input("Ismingizni kiriting: ")
# lastname = input("familyangizni kiriting: ")
# print(f"Sizning ism familyangiz: {firstname} {lastname}")

#Amaliyot
kocha = input("Ko'changizni kiriting: ")
mahalla = input("Mahallangizni kiriting: ")
tuman = input("Tumaningizni kiriting: ")
viloyat = input("Viloyatingizni kiriting: ")
manzil=f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())

