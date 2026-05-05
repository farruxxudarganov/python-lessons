def addition(a, b):
    return a + b

def subtraction(a,b):
    return a - b

def find_max(*number):
    if len(number) == 0:
        return None
    max_value = number[0]
    for son in number:
       if son > max_value:
           max_value = son
    return max_value