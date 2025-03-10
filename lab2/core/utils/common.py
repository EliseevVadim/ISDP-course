import numpy as np

import random
import re

import math


def init_random_seed(value=0):
    np.random.seed(value)
    random.seed(value)


def generate_validation_dictionary(text: str, words_count=None, words_frac=None) -> set:
    words = extract_words(text)
    if words_frac is not None:
        words_count = math.ceil(len(words) * words_frac)
    random.shuffle(words)
    return set(words) if words_count is None or words_count >= len(words) else set(words[:words_count])


def extract_words(text):
    words = re.findall(r"\b[\w'-]+\b", text)
    return words


def display_text_as_table(letters: np.array, key=None, show_key=True):
    key_length = letters.shape[1] if key is None else len(key)
    if show_key and key:
        print("\n" + "=" * (key_length * 4 + 1))
        print("| " + " | ".join(key) + " |")
    print("=" * (key_length * 4 + 1))

    for row in letters:
        print("| " + " | ".join(row) + " |")
        print("-" * (key_length * 4 + 1))


def get_permutation_by_key(key: str):
    sorted_key = sorted(key)
    return [sorted_key.index(char) for char in key]


def preprocess_text(text: str):
    return text.lower().replace('\n', '⏎')


def restore_text(text: str):
    return text.replace('⏎', '\n')
