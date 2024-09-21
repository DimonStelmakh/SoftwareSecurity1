class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet_ua = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
        self.alphabet_en = 'abcdefghijklmnopqrstuvwxyz'

    def validate_key(self):
        # Валідація ключа (має бути цілим числом)
        if not isinstance(self.key, int):
            raise ValueError("Ключ повинен бути цілим числом.")

    def encrypt(self, text, language='ua'):
        # Шифрування тексту
        self.validate_key()
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        shifted_alphabet = alphabet[self.key % len(alphabet):] + alphabet[:self.key % len(alphabet)]
        table = str.maketrans(alphabet, shifted_alphabet)
        return text.translate(table)

    def decrypt(self, text, language='ua'):
        # Розшифрування тексту
        self.validate_key()
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        shifted_alphabet = alphabet[-self.key % len(alphabet):] + alphabet[:-self.key % len(alphabet)]
        table = str.maketrans(alphabet, shifted_alphabet)
        return text.translate(table)


# Приклад використання
# cipher = CaesarCipher(3)
# encrypted_text = cipher.encrypt("привіт", language='ua')
# print("Зашифровано:", encrypted_text)
#
# decrypted_text = cipher.decrypt(encrypted_text, language='ua')
# print("Розшифровано:", decrypted_text)
