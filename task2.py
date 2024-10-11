class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet_ua = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
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


class TrithemiusCipher:
    def __init__(self, A=0, B=0, C=0, key_phrase=None):
        self.A = A
        self.B = B
        self.C = C
        self.key_phrase = key_phrase
        self.alphabet_ua = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        self.alphabet_en = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt_linear(self, text, language='ua'):
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        encrypted_text = []
        for i, char in enumerate(text):
            if char in alphabet:
                step = self.A + self.B * i
                new_pos = (alphabet.index(char) + step) % len(alphabet)
                encrypted_text.append(alphabet[new_pos])
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

    def decrypt_linear(self, text, language='ua'):
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        decrypted_text = []
        for i, char in enumerate(text):
            if char in alphabet:
                step = self.A + self.B * i
                new_pos = (alphabet.index(char) - step) % len(alphabet)
                decrypted_text.append(alphabet[new_pos])
            else:
                decrypted_text.append(char)
        return ''.join(decrypted_text)

    def encrypt_nonlinear(self, text, language='ua'):
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        encrypted_text = []
        for i, char in enumerate(text):
            if char in alphabet:
                step = self.A**2 + self.B * i + self.C
                new_pos = (alphabet.index(char) + step) % len(alphabet)
                encrypted_text.append(alphabet[new_pos])
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

    def decrypt_nonlinear(self, text, language='ua'):
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        decrypted_text = []
        for i, char in enumerate(text):
            if char in alphabet:
                step = self.A ** 2 + self.B * i + self.C
                new_pos = (alphabet.index(char) - step) % len(alphabet)
                decrypted_text.append(alphabet[new_pos])
            else:
                decrypted_text.append(char)
        return ''.join(decrypted_text)

    def encrypt_key_phrase(self, text, language='ua'):
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        key_phrase_repeated = (self.key_phrase * (len(text) // len(self.key_phrase) + 1))[:len(text)]
        encrypted_text = []
        for char, key_char in zip(text, key_phrase_repeated):
            if char in alphabet:
                step = alphabet.index(key_char) + 1
                new_pos = (alphabet.index(char) + step) % len(alphabet)
                encrypted_text.append(alphabet[new_pos])
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

    def decrypt_key_phrase(self, text, language='ua'):
        alphabet = self.alphabet_ua if language == 'ua' else self.alphabet_en
        key_phrase_repeated = (self.key_phrase * (len(text) // len(self.key_phrase) + 1))[:len(text)]
        decrypted_text = []
        for char, key_char in zip(text, key_phrase_repeated):
            if char in alphabet:
                step = alphabet.index(key_char) + 1
                new_pos = (alphabet.index(char) - step) % len(alphabet)
                decrypted_text.append(alphabet[new_pos])
            else:
                decrypted_text.append(char)
        return ''.join(decrypted_text)

