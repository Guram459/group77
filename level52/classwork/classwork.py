# classwork 1

def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    
    return "F"

# Classwork 2

def remove_exclamation_mark(s):
    return s.replace("!", '')

# classwork 3

def no_space(x):
    return x.replace(" ", "")