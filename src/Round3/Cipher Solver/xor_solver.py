cipher_text = "/mnt/p/Python programs/BNA-2025/src/Round3/Part 2/the_accusation.txt"
key = 174

def xor_decrypt(cipher_text, key):
    with open(cipher_text, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = bytearray([b ^ key for b in encrypted_data])
    return decrypted_data.decode('utf-8')

decrypted_message = xor_decrypt(cipher_text, key)
print(decrypted_message)

