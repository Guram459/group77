# Classwork 1

def twice_as_old(dad_years_old, son_years_old):
    return abs(2 * son_years_old - dad_years_old)

# Classwork 2

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

# Classwork 3

def hero(bullets, dragons):
    return bullets >= dragons * 2
