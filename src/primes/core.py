from math import sqrt


def is_prime_v0(num):
    """Brute force version"""
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def is_prime_v1(num):
    if num > 2 and num % 2 == 0:
        return False  # No even numbers other than 2 is prime
    for n in range(2, int(sqrt(num))):
        if num % n == 0:
            return False
    return True


def is_prime_v2(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        n = 5
        while n * n <= num:
            if num % n == 0 or num % (n + 2) == 0:
                return False
            n += 6
        return True
