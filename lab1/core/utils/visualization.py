import numpy as np


def display_text_as_table(letters: np.array, key: str, show_key=True):
    key_length = len(key)
    if show_key:
        print("\n" + "=" * (key_length * 4 + 1))
        print("| " + " | ".join(key) + " |")
    print("=" * (key_length * 4 + 1))

    for row in letters:
        print("| " + " | ".join(row) + " |")
        print("-" * (key_length * 4 + 1))
