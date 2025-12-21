# Classwork 1

def double_integer(i):
    return i * 2

# Classwork 2

def friend(x):
    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result
            

# Classwork 3

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product
        

# Classwork 4

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)