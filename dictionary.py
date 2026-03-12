# Data types (Ma'lumot turlari)
# string , integer , float , list , bool , dictionary
# dictionary - lug'at
car = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964,
    "color": "yellow",
    "price": 45000
}
print(car)
print(type(car)) # 'dict'

user = {
    "fullname": "Farrux Xudarganov",
    "email":"farruxxudarganov1@gmail.com",
    "age": 14,
    "is_student": False,
    "favorite_books": ["Sariq devni minib", "Dunyoni ishlari", "O'tkan kunlar"]
}
# key - value pair(kalit - qiymat juftligi)
# 1. valuelarni olish(key orqali)
print(user["fullname"])
print(user["favorite_books"])
print(user["age"]) 

for book in user["favorite_books"]:
    print(book)

# 2. yangi key - value qo'shish
user['is_married'] = False
user['hobbies'] = ["programming", "playing football", "watching football matches"]
print(user)

# 3. valuelarni o'zgartirish
user["age"] = 15
user["email"] = "xudarganov_f7@gmail.com"

# Bo'sh lug'at(empty dictionary)
talaba_1 = {}

talaba_1["ism"] = "qobil rasulov"
talaba_1["kurs"] = 3
talaba_1["yosh"] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs ")