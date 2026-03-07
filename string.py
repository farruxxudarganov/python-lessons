# # String - matn
# # Data types (Ma'lumot turlari)
# # 1. string(matn) 2.number(son) => 1. integer (butun son)5 -5 0  2. float (o'nli son) 2.5 5.78 -83.99
# # 3. boolean (mantiqiy qiymat) => true (haqiqat); 2. false (yolg'on)
# username = "adminjon" #string
# favourite_number = 77 #number => integer(int)
# is_student = True #boolean

# text="Men yangi 📱 sotib oldim😁"
# print(text)

# region="Xorazm"
# city="Shovot"
# street="Shohsaroy"
# home_number= 71

# #matnlarni birlashtirish
# #Men xorazm viloyati Shovot shahri Shohsaroy ko'chasi 71-uyda yashayman

# # #1-usul: +"Plus" operator yordamida
# # full_adress= "Men " + region + " viloyati " + city + " shahri " + street + " ko'chasi " + str(home_number) + "-uyda yashayman"
# # print(full_adress)
# # #2-usul: f-string yordamida
# # address = f"Men {region} viloyati {city} shahri {street} ko'chasida yashayman"
# # print(address)

# # print('Hello World!')
# # print('Hello \tWorld!') #t-tab
# # print('Hello \nWorld!') #n-new line

# kocha="bog'bon"
# mahalla= "sog'bon"
# tuman="bodomzor"
# viloyat="samarqand"
# full_address= f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."
# print(full_address)
# address= kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani " + viloyat + "viloyati"
# print(address)

firstname = "Farrux"
lastname = "Xudarganov"
#Mening to'liq ism familyam : Farrux Xudarganov
fullname = f"Mening to'liq ism familyam: {firstname} {lastname}"
print(fullname)
fullname2 = "Mening to'liq ism familyam " + firstname + ' ' + lastname
print(fullname2)
