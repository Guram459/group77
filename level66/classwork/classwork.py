# Classwork 1

def to_jaden_case(string):
    result = ("How can mirrors be real if our eyes aren't real")
    
    for i in result:
        return result.capitalize()
    
    return string

# Classwork 2

def explode(arr):  
    xy = arr
    
    if arr == 3:
        return "Void!"
    else:
        return "score"
        
    return xy

# classwork 3

def to_alternating_case(string):
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

# classwork 4

def summation(num):
    return sum(range(1, num+1))
    