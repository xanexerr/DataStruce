# import sys

# #deep copy vs shallow copy
# data = [1,2,3,4,5]

# shallow_copy = data
# deep_copy = data.copy()

# print(f"Data: {data} (id: {id(data)})")
# print("Shallow Copy ก้อบที่อยู่เดียวกันกับ data")
# print(f"Shallow Copy: {shallow_copy} (id: {id(shallow_copy)})")
# print("Deep Copy ก้อบมาสร้าง ที่อยู่ใหม่")
# print(f"Deep Copy: {deep_copy} (id: {id(deep_copy)})")


# # compact Array vs Nprmal Array
# compact_array = [1,2,3,4,5]
# normal_array = [[1,2,3,4,5]]

# print(f"Memory size of compact_array: {sys.getsizeof(compact_array)} bytes")
# print(f"Memory size of normal_array: {sys.getsizeof(normal_array)} bytes")

<<<<<<< HEAD
# เปลี่ยนจาก shift เป็ร "Z Y X W V U T S R Q P O N M L K J I H G F E D C B A"
=======

>>>>>>> 50f18b85098901abd49af8398980987903fb02e1
class CaesarCipher:
        def __init__(self, shift):
                encoder = [None] * 26
                decoder = [None] * 26
                for k in range(26):
                        encoder[k] = chr((k + shift) % 26 + ord('A'))
                        decoder[k] = chr((k - shift) % 26 + ord('A'))  
                self._forward = ''.join(encoder)
                self._backward = ''.join(decoder)
        
        def encrypt(self, message):
                return self._transform(message, self._forward)
        
        def decrypt(self, secret):
                return self._transform(secret, self._backward)
        
        def _transform(self, original, code):
                msg = list(original)
                for k in range(len(msg)):
                        if msg[k].isupper():
                                j = ord(msg[k]) - ord('A')
                                msg[k] = code[j]
                return ''.join(msg)
        
# Example 
cipher = CaesarCipher(3)
<<<<<<< HEAD

=======
>>>>>>> 50f18b85098901abd49af8398980987903fb02e1
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
message = "I dont wanna learn this Classes Any more".upper()
coded = cipher.encrypt(message)
print('Secret:', coded)
answer = cipher.decrypt(coded)
print('Message:', answer)

