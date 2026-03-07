# # # List - ro'yxat
# # fruit1 = 'apple'
# # fruit2 = 'grape'
# # fruit3 = 'banana'
# # print(fruit2)
# # fruits = ['apelsin','grape','banana','apple']
# # print(fruits)
# # print(type(fruits)) # List 
# # #List elementi index orqali olinadi
# # #Dasturlashda index 0 dan boshlanadi
# # #List elementini olish
# # print(fruits[1],fruits[3])
# # mix_data = [12, -5, 5.75, 'test', True]
# # #list elementini o'zgartirish
# # fruits[1] = 'cherry'
# # print(fruits)
# # #list uzunligi (length) - ro'yxatda saqlangan elementlar soni
# # print(len(fruits))
# # print(len(mix_data))
# # #listdagi so'ngi elementni topish
# # length=len(mix_data)
# # print(mix_data[length - 1])
# # #first element 
# # print(mix_data[0])
# # #last element
# # length = len(mix_data)
# # last_index = length -1
# # last_element = mix_data[last_index]
# # print(last_element)

# # Royxat  elementlari ustida amallar
# numbers = [12, -15, 88.99, 10, 15.93, -8.75]
# # 1.Ro'yxat elementini o'zgartirish
# numbers[1] = 20

# # Ro'yxatga yangi element qo'shish
# #2 list.append(new_element) method
# numbers.append(17)
# numbers.append(-102.89)
# print(numbers)

# #1. list.insert(index. new_element) method
# numbers.insert(2, 13)
# print(numbers)
# numbers.insert(0, 0)
# print(numbers)

# #CRUD - create / read / update / delete
# #Ro'yxat elementini o'chirish
# # 1. list.remove(element)
# numbers.remove(0)
# print(numbers)
# numbers.remove(numbers[3])
# print(numbers)

# #del operatori 
# del numbers[5]
# print(numbers)

# #Ro'yxatdagi elemendlarni sug'urib olish
# # list.pop(index?) methon
# number = numbers.pop(2)
# print(number)
# print(numbers)
# last_element=numbers.pop()
# print(last_element)

# 1-topshiriq
ismlar=["Nurali","Feruzbek","Behruz"]
print("Qandaysan " + ismlar[0]+ ", ishlaring yaxshim " + ismlar[1] + ", Nima qilyabsan " + ismlar[2])
# 2-topshriq
sonlar=[12, 17, 7, -12, 19.69, 67]
# 3-topshriq
sonlar[3]=100
print(sonlar)
sonlar.append(28)
print(sonlar)
# 4-topshiriq
t_shaxslar = ["Amir Temur", "Alisher Navoiy", "Islom Karimov", "Abu Rayxon Beruniy"]
z_shaxslar = ["Shavkat Mirziyoyev", "Cristiano Ronaldo", "Lionel Messi", "Odil Ahmedov", "Eldor Shomurodov", "Elon Musk"]
# 5-topshiriq
t_shaxslar.pop(0)
z_shaxslar.pop(1)
print(t_shaxslar)
print(z_shaxslar)
# 6-topshriq
friends=[]
friends.append("Nurali")
friends.append("Shoxrux")
friends.append("Jonibek")
print(friends)
#  7-topshiriq
friends.remove("Shoxrux")
print(friends)
# 8-topshiriq   
friends.append("Elyor")
friends.insert(0, "Jo'shqin")
friends.insert(3, "Dilmurod")
print(friends)
# 9-topshiriq
mehmonlar=[]
mehmonlar.append("Nurali")
mehmonlar.append("Shoxrux")
mehmonlar.append("Jonibek")
mehmonlar.pop("Jonibek")
