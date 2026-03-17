# # Dictionary elementlari bilan ishlash
# phone = {
#     "brand": "Apple",
#     "model": "iPhone 13 Pro",
#     "color": "Silver",
#     "storage": "256GB",
#     "price": "$1500"
# }
# # get() medodi - kalit orqali qiymatni olish
# print(phone.get("model")) # iPhone 13 Pro
# print(phone.get("price", "Narx topilmadi")) # $1500
# print(phone.get("battery", "Kalit topilmadi")) # None , chunki "battery" kaliti lug'atda mavjud emas

# # items() metodi - lug'at elementlarini (kalit va qiymat juftligini) olish
# print(phone.items()) # dict_items([('brand', 'Apple'), ('model', 'iPhone 13 Pro'), ('color', 'Silver'), ('storage', '256GB'), ('price', '$1500')])
# for key, value in phone.items():
#     print(f"Kalit: {key}, Qiymat: {value}")
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# print(phone.keys()) # dict_keys(['brand', 'model', 'color', 'storage', 'price'])
# print(telefonlar.keys()) # dict_keys(['ali', 'vali', 'olim', 'orif'])

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# # in operatori 
# # 2. list element;ari orasida qiymat mavjudligini tekshirish
# # 3. Kalit lug'atda mavjudligini tekshirish
bozorlik = ['anor', 'uzum', 'anjir', 'shaftoli']
# print('anor' in bozorlik) # True
# print('olma' in bozorlik) # False

# mahsulot = input("Qaysi mahsulotni sotib olmoqchisiz? ")
# if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} do'konimizda bor")
# else:
#         print(f"{mahsulot.title()} do'konimizda yo'q")
# for mahsulot in mahsulotlar:
#     # print(mahsulot)
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} do'konimizda bor")
#     else:
#         print(f"{mahsulot.title()} do'konimizda yo'q")

# # lug'at elementlarini tartib bilan chiqarish 
print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
for narx in mahsulotlar.values():
    print(narx)
