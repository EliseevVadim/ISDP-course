import random

from core.utils import letter_to_binary, generate_gamma, xor_columns, polynom, lagrange_interpolation, \
    chinese_remainder_theorem, generate_coprime_primes


def secret_multilateral_protocol(encryption_params: list[dict]):
    x = random.randint(0, encryption_params[0]['n'] // 2)
    step_value = 0
    for i, encryption_param in enumerate(encryption_params):
        print(f"Шифрование агентом №{i + 1}:\n")
        e = encryption_params[0]['e'] if i + 1 == len(encryption_params) else encryption_params[i + 1]['e']
        if i == 0:
            new_x = x
            print(f'x = {x}')
            step_value = pow(encryption_param['code'] + new_x, e, encryption_param['n'])
            print(f"({encryption_param['code']} + {new_x}) ** {e} mod {encryption_param['n']} = {step_value}")
            continue
        new_x = pow(step_value, encryption_param['d'], encryption_param['n'])
        print(f'x = {step_value} ** {encryption_param["d"]} % {encryption_param["n"]} = {new_x}')
        step_value = pow(encryption_param['code'] + new_x, e, encryption_param['n'])
        print(f"({encryption_param['code']} + {new_x}) ** {e} mod {encryption_param['n']} = {step_value}\n")

    print("Расшифровка результата:\n")
    final_value = pow(step_value, encryption_params[0]['d'], encryption_params[0]['n'])
    print(f"{step_value} ** {encryption_params[0]['d']} % {encryption_params[0]['n']} = {final_value}")
    print(f"({final_value} - {x}) / {len(encryption_params)} = {(final_value - x) / len(encryption_params)}\n")
    return (final_value - x) / len(encryption_params)


def gamma_secret_split_protocol(secret: list[str], n_gammas=3):
    codes = [letter_to_binary(letter) for letter in secret]
    print('Исходные коды:\n')
    print(codes)
    print()
    gammas = [generate_gamma() for _ in range(n_gammas)]
    print('Гаммы:\n')
    print(gammas)
    print()
    gamma_codes = [[letter_to_binary(letter) for letter in gamma] for gamma in gammas]
    print('Гаммы в закодированном виде:\n')
    print(gamma_codes)
    print()
    encrypting_codes = gamma_codes.copy()
    encrypting_codes.insert(0, codes)
    print('Коды шифрования\n')
    print(encrypting_codes)
    print()
    encrypted = xor_columns(encrypting_codes)
    print('Зашифрованные коды:\n')
    print(encrypted)
    print()
    decrypting_codes = gamma_codes.copy()
    decrypting_codes.append(encrypted)
    print('Коды дешифрования\n')
    print(decrypting_codes)
    print()
    decrypted = xor_columns(decrypting_codes)
    print('Дешифрованные коды:\n')
    print(decrypted)
    return decrypted, codes


def shamir_split_protocol(secret: int, n: int, m: int, p: int):
    coefficients = [secret] + [random.randint(0, p - 1) for _ in range(m - 1)]
    print("Коэффициенты полинома:\n")
    print(coefficients)
    print()
    shares = []
    for i in range(1, n + 1):
        x = i
        y = polynom(x, coefficients) % p
        shares.append((x, y))
    print("Сгенерированные доли:\n")
    print(shares)
    return shares


def shamir_recover(shares: list, p: int):
    x_s, y_s = zip(*shares)
    print("Используем доли для восстановления секрета:\n")
    print(shares)
    print()
    return lagrange_interpolation(0, x_s, y_s, p)


def secret_sharing_scheme(secret: int, n: int, m: int, p: int):
    d = generate_coprime_primes(p, n)

    # Вычисляем минимальный множитель r
    product_d = 1
    for di in d:
        product_d *= di

    r = (product_d - secret) // p
    if (secret + r * p) < product_d:
        r += 1

    S_prime = secret + r * p

    shares = [(di, S_prime % di) for di in d]

    print("Таблица долей (di, ki):")
    for di, ki in shares:
        print(f"({di}, {ki})")

    print(f"\nПубликуем p: {p}")

    return d, [ki for _, ki in shares]


def secret_recovery(d, shares):
    print("\nВосстановление секрета с помощью китайской теоремы об остатках...")

    secret_recovered = chinese_remainder_theorem(d, shares)

    return secret_recovered
