def caesar_cipher(text, shift):
    result = ""

    for character in text:
        if character.isalpha():
            base = ord('A') if character.isupper() else ord('a')

            shifted_character = chr(
                (ord(character) - base + shift) % 26 + base
            )

            result += shifted_character
        else:
            result += character

    return result


def encrypt(text, shift):
    return caesar_cipher(text, shift)


def decrypt(text, shift):
    return caesar_cipher(text, -shift)


if __name__ == "__main__":
    print("=== Caesar Cipher ===")

    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(text, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted:", encrypted)
    print("Decrypted:", decrypted)