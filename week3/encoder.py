class CaesarCipher:
        # old shifter
        #     def __init__(self, shift):
        # encoder = [None] * 26
        # decoder = [None] * 26
        # for k in range(26):
        #     encoder[k] = chr((k + shift) % 26 + ord('A'))
        #     decoder[k] = chr((k - shift) % 26 + ord('A'))
        # self._forward = ''.join(encoder)  # Encryption string
        # self._backward = ''.join(decoder)  # Decryption string
    def __init__(self, shift):
        encoder = shift.split()
        self._forward = ''.join(encoder)
        self._backward = ''
        for i in range(26):
            self._backward += chr(ord('A') + encoder.index(chr(ord('A') + i)))

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, message):
        return self._transform(message, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


# Example usage:
shift_key = "D E F G H I J K L M N O P Q R S T U V W X Y Z A B C"

cipher = CaesarCipher(shift_key)
message = "HELLO WORLD"

coded = cipher.encrypt(message)
print('Secret:', coded)
answer = cipher.decrypt(coded)
print('Message:', answer)
