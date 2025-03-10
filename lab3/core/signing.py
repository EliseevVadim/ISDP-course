import random

from core.utils import calculate_hash


def sign_message(message, dsa_parameters):
    q, p, g, x, _ = dsa_parameters
    hashed_message = calculate_hash(message, g)
    while True:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        s = (pow(k, -1, q) * (hashed_message + x * r)) % q
        if s != 0:
            return r, s


def verify_signature(message, r, s, dsa_parameters):
    q, p, g, _, y = dsa_parameters
    if not (0 < r < q and 0 < s < q):
        raise ValueError('Параметры подписи были выбраны неверно')
    hashed_message = calculate_hash(message, g)
    w = pow(s, -1, q)
    u1 = (hashed_message * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r
