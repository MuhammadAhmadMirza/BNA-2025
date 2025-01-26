#  make a program to solve ceaser cipher

ciphertext = "/mnt/p/Python programs/BNA-2025/src/Round3/Part 2/the_reason.txt"
shift = 17

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

with open(ciphertext, 'r') as file:
    encrypted_message = file.read()

decrypted_message = decrypt_caesar_cipher(encrypted_message, shift)

print(decrypted_message)