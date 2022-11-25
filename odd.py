from even import is_even

def is_odd(n):
    if is_even(n):
        return False
    return True

print(is_odd(11))
print(is_odd(10))
