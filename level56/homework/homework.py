# Classwork 1

def main (verb, noun):
    return verb + noun

# Classwork 2

def area_or_perimeter(l , w):
    if l == w:
        return w * l
    else:
        return w * 2 + l * 2
    
# Classwork 3

def opposite(number):
    return -number

# Classwork 4

def boolean_to_string(b):
    if b == 1:
        return 'True'
    else:
        return 'False'
    
# Classwork 5

def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4