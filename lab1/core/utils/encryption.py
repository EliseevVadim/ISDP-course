from core.utils.common import *
from core.utils.visualization import *


class Encryptor:
    def __init__(self, text: str, key_path: str, output_path: str, max_key_length=10,
                 base_block_size=8, pad_symbol=' '):
        self.text = preprocess_text(text)
        self.key_path = key_path
        self.output_path = output_path
        self.pad_symbol = pad_symbol

        self.__input_length = len(text)
        self.__key_length = None

        self.block_size = next_multiple(int(self.__input_length / max_key_length), base_block_size)

    def __convert_text_to_array(self):
        letters = np.array(list(self.text))
        self.__key_length = (self.__input_length + self.block_size - 1) // self.block_size
        chars_to_pad = self.block_size * self.__key_length - self.__input_length
        if chars_to_pad > 0:
            letters = np.append(letters, [self.pad_symbol] * chars_to_pad)
            self.__key_length = len(letters) // self.block_size
        return letters

    def encrypt(self, show_key=False, verbose=False):
        letters = self.__convert_text_to_array()
        key = generate_and_save_random_key(self.__key_length, self.key_path)
        permutation_order = get_permutation_by_key(key)
        letters = letters.reshape(self.block_size, self.__key_length)
        if verbose:
            print("\nИсходный текст в табличном представлении при сгенерированном ключе:")
            display_text_as_table(letters, key, show_key=show_key)

        letters = letters[:, permutation_order]
        key = ''.join(sorted(key))
        if verbose:
            print("\nИсходный текст в зашифрованном виде:")
            display_text_as_table(letters, key, show_key=show_key)
        write_encrypted_text_to_file(letters, self.output_path)
        print("Текст успешно зашифрован и записан в файл\n")
