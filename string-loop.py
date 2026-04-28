text = "Python Lessons"
# print(len(text)) # 14
# string ichidagi har bir belgi indeksga ega (0 dan boshlanadi)
# print(text[0]) # P
# print(text[1]) # y
# print(text[2]) # t
# print(text[6]) #  
# print(text[13]) # s
# print(text[-1]) # s
# print(text[-2]) # n
# string ichidagi oxirgi belgi indeks olish uchun -1 dan foydalaniladi
# print(text[len(text)-1]) # s
# for tsikl
# 1-usul
# for belgi in text:
#     print(belgi)
# # 2-usul
# for index in range(len(text)):
#     print(index , text[index])


# txt = "Bugun darsga Xursandbek kelmadi"
# #  in operatori - string ichida ma'lum bir belgining bor yoki yo'qligini tekshirish uchun ishlatiladi
# print("Xursandbek" in txt) # True
# print("Asadbek" in txt) # False
# print("y" in txt) # False
# print("a" in txt) # True

# unli haflar (a, e, i, o, u)
# Example "Salom" -> 2 unli harf(a, o)

# vowels = "aeiou"
# def count_vowels(word):
#     count= 0
#     for letter in word.lower():
#         if letter in vowels:
#             count += 1
#     return count
# print(count_vowels("Salom"))  # Output: 2
# print(count_vowels("Python")) # Output: 1
# print(count_vowels("bbb"))   # Output: 0

