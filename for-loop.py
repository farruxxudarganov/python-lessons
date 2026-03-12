# # Loop - sikl
# # 1.for loop # 2. while loop
# students = ["Charos", "Kumush", "Akmal", "Ozodbek", "Xudoyshukur", "Asal"]
# for student in students:
#     print(f"Hurmatli {student}, sizni interviewga taklif etamiz")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi")

# # nums = list(range(1, 11))
# # for number in nums:
# #     # print(number)
# #     print(f"{number} sonining kvadrati {number**2} ga teng")

# sonlar = list(range(20))
# # print(sonlar)
# # start_default_value = 0
# print(sonlar) #[0, 1, ... 18, 19]
# # [0, 1, 4, 9, 16 ... 324, 361]
# sonlar2 = []
# for son in sonlar:
#     sonlar2.append(son**2)

# print(sonlar2)


# # 2 - usul

# for index in range(len(sonlar)):
#     print(index) # element indexi
#     print(sonlar[index]) # element

# # 1-marta -> index - 0 -> sonlar[0] = 0
# # 2-marta -> index - 1 -> sonlar[1] = 1
# # 3-marta -> index - 2 -> sonlar[2] = 2
# # ...
# # 20-marta -> index - 19 -> sonlar[19] = 19

# sonlar3 = list(range(1,101))
# for element in sonlar3:
#     print(element)

# for  number in range(1,101):
#     print(number)

# name = ["Ali","Vali","Hasan","Husan","Nurali"]
# for names in name:
#     print(f"Qalaysan {names}")

# print(f"Kod {len(names)} marta takrorlandi")


# numbers = list(range(11,100,2))
# for number in numbers:
#     print(number ** 3)

# kinolar = []
# for kino in range(5):
#     kinolar.append(input(f"{kino+1} - kinoni kiriting: "))
# print(kinolar)

# inson_soni = int(input("Bugun nechta odam bilan uchrashdingiz: "))
# insonlar = []
# for n in range(inson_soni):
#     inson = input(f"{n+1} - insonni ismini kiriting: ")
#     insonlar.append(inson)
# print(insonlar)



# dost_soni = int(input("Nechta do'stingiz bor : "))
# dostlar = []
# for n in range(dost_soni):
#     dost = input(f"{n+1} - Do'stingizni ismini kiriting: ")
#     dostlar.append(dost)
# print(f"Sizning do'stlaringiz {dostlar}")

# telefonlar = []
# for n in range(4):
#     telefon = input(f"{n+1} - Telefon nomini kiriting: ")
#     telefonlar.append(telefon)
# print(f"Siz yoqtirgan telefonlar {telefonlar}")

# numbers = [69,18,89,12,75,82,5,26]
# # nums = []
# # min_value = min(numbers)
# # for number in numbers:
# #     nums.append(number / min_value)
# # print(nums)

# s = 0 
# for number in numbers:
#     s += number
# print(s)
# s=0
# for m in range(2,50,2):
    # s += m
# print(s)

# n! = 1 * 2* 3 * ... (n - 1) * n
# kopaytma = 1
# s=0
# for son in range(1,20,2):
    # kopaytma *= son
    # s+=son
# print(kopaytma / s)


# s = 0 
# for son in nums:
#     s+=son**2
# print(s)

# nums = [24,50,72,96,95]
# s = 0
# for n in nums:
    #  s+=n
# lenth = len(nums)
# print(s / lenth)

# nums = [12, -5, 15, 89, -75 ,0, -18]
# s=0
# k=1
# for son in nums:
#     if son > 0:
#         s+=son
#     else:
#         k*=son

# print(s)
# print(k)
# import math
# nums = [12, -5, 15, 89, -75 , -18]
# s = 0
# for n in nums:
#     s+=n
# lenth = len(nums)
# print(s / lenth)

# kopaytma=1
# for number in nums:
#     kopaytma*=number
# length = len(nums)
# a=math.pow(kopaytma, 1 / length)
# print(a)

# nums = [97, 97, -92, 14, 22]
# s=0
# for n in nums:
#     if n%2==0 or n%3==0 or n%5==0:
#            s+=n
# print(s)

# import math
# numbers= [44,34,42,83,43,64]
# kopaytma=1
# for n in numbers:
#     if n%2==0 or n%5==0:
#         kopaytma*=n
# print(math.sin(kopaytma))

# numbers = [93,64,-90,74,62,-83,58,15,-37]
# s=0
# for n in numbers:
#     if n<0:
#         s+=n
#         lenght = len(s)
# print(s/lenght)

# numbers = [12, 88, 30, 87]
# m = int(input("Sonni kiriting: "))
# s = 0
# for n in numbers:
#     if n>m:
#         s+=n
# print(s)

# m=int(input("Son kiritng: "))
# nums = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# s=0
# for n in nums:
#     if n<m:
#         s+=n ** 2
# print(s)

# nums = [44, 59, -75, 73]
# s=0
# k=0
# length = len(nums)
# for n in nums:
#     s+=n ** 2 
#     k+=n 
# print(s)
# print(k/length)
# import math
# numbers = [7, 24, -5, 23, 99, -3, 24, 51]
# s=0
# for number in numbers:
#     s=+number
# average_value = s / len(numbers)
# log_value = math.log(average_value)
# print(log_value)
# for  index in range(len(numbers)):
#     if numbers[index] <0:
#         numbers[index] = log_value
# print(numbers)

# 124
# numbers = [29, 50, -14, 4, 27, -56]
# k = int(input("Elementni o'rnini kiritng: "))
# Plan
# 1. max elementni topish 
# 2. max elementni indexini topish
# 3. k o'rindagi element bilan max elment o'rnini almashtirish
# max_value = max(numbers)
# max_index = numbers.index(max_value)
# numbers[4]
# numbers[max_index] = numbers[k-1]
# numbers[k-1] = max_value
# print(numbers)

a = 5 
b = 3
# natija: a = 3; b = 5
# 1-usul
# temporary variable - vaqtinchalik o'zgaruvchi 
# c = a
# a = b
# b = c 
# print(a, b)

# 2 - usul
# a, b = b, a 
# print(a, b)

# 3 - usul 
[a,b] = [b, a]
print(a, b)
