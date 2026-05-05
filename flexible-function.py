# # return function
# def sum_list(lst):
#     s = 0
#     for number in lst:
#         s+=number
#     return s
# print(sum_list([15, -5, 8, 7, 0]))

# flexible(moslashuvchan) function
#  *args **kwargs
# *args
# def summa(*sonlar):
#     # print(sonlar)
#     # print(type(sonlar)) #tuple
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(8, 9, 12, -5, 89, 100))
# print(summa(7, -5, -2))

# def my_function(greeting, *names):
#     for name in names:
#         print(greeting, name)
    
# my_function("Hello", "Emil", "Tobias", "Linus")

# def summa(x,y, *sonlar):
#     return x + y + sum(sonlar):
# print(summa(1, 7, 1, -5, -2))
# print(summa(2))

# **kwargs
# def avto_info(kompaniya, model, **malumotlar):
#     # print(malumotlar) # {'key': value}
#     # print(type(malumotlar)) #dict
#      malumotlar['kompaniya'] = kompaniya
#      malumotlar['model'] = model

#      return malumotlar
# print(avto_info("GM Uzbekistan", "Onix", rang='qora', yil='2025'))
# print(avto_info("Kia", "K5", rang='qizil', narh=35000))


# def my_function(**kid):
#     print("His last name is " + kid("lname"))

# my_function(fname = 'Tobias', lname = 'Refsnes')
# 1
# def multiply(*num):
#     s=1
#     for nums in num:
#         s *= nums
#     return s
# print(multiply(2, 4, 2, 6, 7, 1, 10))


# # 2
# def student_name(fname, lname, **malumotlar):
#     malumotlar['ism'] = fname
#     malumotlar['familiya'] = lname

#     return malumotlar
# print(student_name("Ali", "Valiyev", yosh='19'))

def find_max(*number):
    if len(number) == 0:
        return None
    max_value = number[0]
    for son in number:
       if son > max_value:
           max_value = son
    return max_value
print(find_max(1,5,12,17,61,12,21))

