# Classwork 1

def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# Classwork 2

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

# Classwork 3

def cap_me(arr):
    new_list = []
    for name in arr:
        new = name.capitalize()
        new_list.append(new)
    return new_list

# Classwork 4

def solution(s):
    results = ""
    for i in s:
        if i != i.lower():
            results += " " + i
        else:
            results += i
    return results