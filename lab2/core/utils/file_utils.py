import numpy as np


def read_plain_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().strip()


def write_plain_text_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def read_encrypted_text_from_file(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [list(line.rstrip('\n')) for line in f.readlines()]

    return np.array(lines)
