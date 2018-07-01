
NUMS = {2: True, 3: True, 4: False, 5: True, 6: False, 4583: True, 4584: False}


def test_is_prime_v0():
    from primes import is_prime_v0
    for num, is_prime in NUMS.items():
        assert is_prime_v0(num) == is_prime


def test_is_prime_v1():
    from primes import is_prime_v1
    for num, is_prime in NUMS.items():
        assert is_prime_v1(num) == is_prime


def test_is_prime_v2():
    from primes import is_prime_v2
    for num, is_prime in NUMS.items():
        assert is_prime_v2(num) == is_prime
