def is_leap_year(n):
    if n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 400 == 0:
        return True
    elif n % 4 == 0 and n % 100 == 0 and n % 400 != 0:
        return False
    return False

print(is_leap_year(1984))