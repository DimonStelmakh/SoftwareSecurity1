class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet_ua = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
        self.alphabet_en = 'abcdefghijklmnopqrstuvwxyz'

    def validate_key(self):
        if not isinstance(self.key, int):
            raise ValueError("Ключ повинен бути цілим числом!")

    def encrypt(self, text, language='ua'):
        self.validate_key()
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        shifted_alphabet = alphabet[self.key % len(alphabet):] + alphabet[:self.key % len(alphabet)]
        table = str.maketrans(alphabet, shifted_alphabet)
        return text.translate(table)

    def decrypt(self, text, language='ua'):
        self.validate_key()
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        shifted_alphabet = alphabet[-self.key % len(alphabet):] + alphabet[:-self.key % len(alphabet)]
        table = str.maketrans(alphabet, shifted_alphabet)
        return text.translate(table)

