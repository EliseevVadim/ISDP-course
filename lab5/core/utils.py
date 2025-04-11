import random
import numpy as np
import sympy as sp

from core.constants import BOUNDARIES_MAP


def init_random_seed(seed=0):
    random.seed(seed)
    np.random.seed(seed)


def letter_to_code(letter: str, lang='ru'):
    if lang not in ['ru', 'en']:
        raise ValueError(f'Invalid language code: {lang}')
    if letter.isupper():
        start_code = ord('A') if lang == 'eng' else ord('А')
    else:
        start_code = ord('a') if lang == 'eng' else ord('а')
    result = ord(letter) - start_code + 1
    return result if result <= 6 else result + 1 # обрабатываем букву ё


def letter_to_binary(letter: str, encoding='windows-1251'):
    byte_value = letter.encode(encoding)
    return format(byte_value[0], '08b')


def binary_to_letter(binary_str, lang='ru', encoding='windows-1251'):
    byte_value = int(binary_str, 2)
    if lang not in ['ru', 'en']:
        raise ValueError(f'Invalid language code: {lang}')
    if lang == 'ru':
        return bytes([int(binary_str, 2)]).decode(encoding)
    return chr(int(binary_str, 2))


def generate_gamma(size=3, lang='ru', is_upper=True):
    if lang not in ['ru', 'en']:
        raise ValueError(f'Invalid language code: {lang}')
    case = 'upper' if is_upper else 'lower'
    start = BOUNDARIES_MAP[lang][case]['start']
    end = BOUNDARIES_MAP[lang][case]['end']

    letters = [chr(code) for code in range(start, end)]
    return random.choices(letters, k=size)


def xor_columns(matrix):
    arr = np.array([[list(map(int, list(b))) for b in row] for row in matrix])
    xor_result = np.bitwise_xor.reduce(arr, axis=0)
    return [''.join(map(str, col)) for col in xor_result]


def polynom(x, coefficients):
    result = 0
    for power, coeff in enumerate(coefficients):
        result += coeff * (x ** power)
    return result


def lagrange_interpolation(x, x_s, y_s, prime):
    total = 0
    print(f"Процесс интерполяции для x = {x}:")
    for i in range(len(x_s)):
        xi, yi = x_s[i], y_s[i]
        prod = yi
        print(f"  Применение к точке ({xi}, {yi}):")
        for j in range(len(x_s)):
            if i != j:
                xj = x_s[j]
                print(f"    Умножаем на (x - {xj}) / ({xi} - {xj})...")
                prod *= (x - xj) * pow(xi - xj, -1, prime)
                prod %= prime
        total += prod
        total %= prime
        print(f"  Промежуточная сумма для точки {i}: {total}")
    return total


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Обратный элемент не существует")
    return x % m


def generate_coprime_primes(start, count):
    primes = []
    p = sp.nextprime(start - 1)
    while len(primes) < count:
        primes.append(p)
        p = sp.nextprime(p)
    return primes


def chinese_remainder_theorem(n, a):
    total = 0
    prod = 1
    for ni in n:
        prod *= ni

    for ni, ai in zip(n, a):
        p = prod // ni
        total += ai * mod_inverse(p, ni) * p

    return total % prod
