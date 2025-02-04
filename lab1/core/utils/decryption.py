from core.utils.common import *
from core.utils.visualization import *


class Decryptor:
    def __init__(self, encrypted_text_path: str, key_path: str, output_path: str):
        self.letters = read_encrypted_text_from_file(encrypted_text_path)
        self.key = read_plain_text_from_file(key_path)
        self.output_path = output_path

    def decrypt(self, show_key=False, verbose=False):
        if verbose:
            print("\nИсходный текст в зашифрованном виде:")
            display_text_as_table(self.letters, self.key, show_key=show_key)
        permutation_order = get_permutation_by_key(self.key)
        inverse_permutation = np.argsort(permutation_order)
        self.letters = self.letters[:, inverse_permutation]
        if verbose:
            print("\nИсходный текст в табличном представлении при заданном ключе:")
            display_text_as_table(self.letters, self.key, show_key=show_key)
        decrypted_letters = self.letters.flatten()
        decrypted_text = restore_text(''.join(decrypted_letters))
        print("\nРасшифованный текст:\n")
        print(decrypted_text)
        write_plain_text_to_file(self.output_path, decrypted_text)
        print("\nРасшифрованный текст успешно записан в файл\n")
