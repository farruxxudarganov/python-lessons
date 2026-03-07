# #list  bilan ishlash 
# # list methods
# # 1. list.append(element)
# # 2. list.insert(index, element)
# # 3. list.remove(element)
# # 4. list.pop(index?)
# # 5. list.sort() 
# cars = ['bmw','mercedes benz', 'volvo', 'damas', 'general motors', 'tesla', 'audi']
# # cars.sort() #Alifbo(ingliz) ketma-ketlik bo'yicha tartiblash
# # print(cars)
# # cars.sort(reverse=True) # reverse(Teskari)
# print(cars)

# sorted_list=sorted(cars)
# print(sorted_list)
# reversed_sorted_list=sorted(cars, reverse=True)
# print(reversed_sorted_list)

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort() #O'shish tartibi 
# print(ages)
# print(sorted(ages, reverse=True)) #Kamayish tartibi

# # list.reverse()
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
# print(len(fruits)) # 5

# # list() funksiyasi

# # range() funksiyasi - ma' lum bir oraliqdagi sonlarni shakllantirish uchun ishlatilinadi
# # range(start,stop,step)
# # sterp = 1-(default value)
# # range(0,10)  
# sonlar = list(range(0, 10))
# juft_sonlar= list(range(2,21,2))
# print(sonlar)
# print(juft_sonlar)

# # min(), max(), sum()
# narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# eng_arzon = min(narxlar)
# eng_qimmat = max(narxlar)
# print(eng_arzon)
# print(eng_qimmat)
# yigindi = sum(narxlar)
# print(yigindi)

# # listni kesish
# techs = ['AI','Robot', 'Python', 'DB', 'Chat GPT','Web']
# my_tech = techs[2:5]
# print(my_tech)
# print(techs[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(techs[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi



# Amaliyot
davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Saudiya", "Angliya", "AQSh"]
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
son = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
eng_katta = max(son)
eng_kichik= min(son)
print(eng_katta + eng_kichik)
print(eng_katta-eng_kichik)

sonlar = list(range(120, 1200, 2))
print(sonlar)
print(sum(sonlar))

print(len(sonlar))

print(sonlar[:20])
print(sonlar[-20:])
length=len(sonlar)
start_index= length // 2 -10
end_index= length // 2 + 10
print(sonlar[start_index : end_index])
