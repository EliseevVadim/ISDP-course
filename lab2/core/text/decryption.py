import numpy as np

from core.utils.common import *
from core.utils.file_utils import *


class Decryptor:
    def __init__(self, letters: np.array, key: str):
        self.letters = letters
        self.__key = key

    def decrypt(self, show_key=False, verbose=False) -> str:
        if verbose:
            print("\nИсходный текст в зашифрованном виде:")
            display_text_as_table(self.letters, ''.join(sorted(self.__key)), show_key=show_key)
        permutation_order = get_permutation_by_key(self.__key)
        inverse_permutation = np.argsort(permutation_order)
        self.letters = self.letters[:, inverse_permutation]
        if verbose:
            print("\nИсходный текст в табличном представлении при заданном ключе:")
            display_text_as_table(self.letters, self.__key, show_key=show_key)
        decrypted_letters = self.letters.flatten()
        decrypted_text = restore_text(''.join(decrypted_letters))
        return decrypted_text

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key
