import numpy as np

import random
import string

from core.utils.file_utils import *


def init_random_seed(value=0):
    np.random.seed(value)
    random.seed(value)


def generate_and_save_random_key(length: int, key_path: str):
    key = ''.join(random.sample(string.ascii_uppercase, length))
    write_plain_text_to_file(key_path, key)
    print("Ключ был успешно сгенерирован и записан")
    return key


def get_permutation_by_key(key: str):
    sorted_key = sorted(key)
    return [sorted_key.index(char) for char in key]


def next_multiple(number: int, n: int) -> int:
    return ((number + n - 1) // n) * n


def preprocess_text(text: str):
    return text.replace('\n', '⏎')


def restore_text(text: str):
    return text.replace('⏎', '\n')
