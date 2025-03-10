import random

from core.utils import is_prime_rabin_miller


def generate_challenge(lower_limit, upper_limit):
    return str(random.randint(lower_limit, upper_limit))


def generate_prime(bits=50):
    while True:
        number = random.getrandbits(bits) | 1
        if is_prime_rabin_miller(number):
            return number


def generate_dsa_parameters(bits=50):
    q = generate_prime(bits // 2)
    k = 2
    while True:
        p = k * q + 1
        if is_prime_rabin_miller(p):
            break
        k += 1
    g = pow(random.randint(2, p - 1), (p - 1) // q, p)
    x = random.randint(1, q - 1)
    y = pow(g, x, p)
    return q, p, g, x, y
