import itertools
import string
import time

from core.text.decryption import Decryptor
from core.utils.file_utils import read_encrypted_text_from_file
from core.utils.common import *


def generate_keys(key_length):
    return ("".join(sequence) for sequence in itertools.product(string.ascii_uppercase, repeat=key_length))


class CipherBreaker:
    def __init__(self, encrypted_text_path: str, validator: set):
        self.encrypted_text = read_encrypted_text_from_file(encrypted_text_path)
        self.validator = validator

        print("Шифр-текст успешно загружен:")
        display_text_as_table(self.encrypted_text)

    def hack_by_key_brute_force(self, timeout=3600) -> str:
        start_time = time.time()
        attempts = 0
        for key in generate_keys(key_length=self.encrypted_text.shape[1]):
            if time.time() - start_time > timeout:
                print(f"Не получилось взломать шифр за отведенное время {timeout} сек. Было "
                      f"совершено попыток {attempts}")
                raise TimeoutError
            decryptor = Decryptor(self.encrypted_text, key=key)
            decrypted_text = decryptor.decrypt()
            attempts += 1
            if self.__decryption_is_valid(decrypted_text):
                print(f"Подходящий ключ успешно найден! Ключ: {key}")
                print(f"Подходящий ключ был найден за число попыток: {attempts}")
                return decrypted_text
        print(f"Не удалось взломать шифр путем перебора ключей. Было совершено попыток: {attempts}")

    def __decryption_is_valid(self, decrypted_text: str):
        words = extract_words(decrypted_text)
        return self.validator.issubset(words)
