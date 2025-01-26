# Atbash Cipher, Symmetrical Alphabetic Substitution [ A ---> Z, B ---> Y ]

file = "/mnt/p/Python programs/BNA-2025/src/Round3/Part 2/the_truth.txt"
with open(file, 'r') as f:
    cipher_text = f.read()

def atbash_cipher(text):
    def translate(char):
        if char.isalpha():
            return chr(155 - ord(char)) if char.isupper() else chr(219 - ord(char))
        return char

    return ''.join(translate(c) for c in text)

plain_text = atbash_cipher(cipher_text)
print(plain_text)