def encrypt(text, key):
    encrypted_text = ""

    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if it's an uppercase or lowercase letter
            is_upper = char.isupper()
            
            # Convert the letter to its ASCII code, apply the shift, and convert back to a letter
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + key) % 26 + ord('A' if is_upper else 'a'))
            
            encrypted_text += shifted_char
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char

    return encrypted_text

# Example usage:
plaintext = "Hello, World!"
shift_key = 3
encrypted_result = encrypt(plaintext, shift_key)

print(f"Original Text: {plaintext}")
print(f"Encrypted Text: {encrypted_result}")

def decrypt(encrypted_text, key):
    decrypted_text = ""

    # Use the encrypt function with a negative key to perform decryption
    decrypted_text = encrypt(encrypted_text, -key)

    return decrypted_text

# Example usage:
encrypted_text = "Khoor, Zruog!"
shift_key = 3
decrypted_result = decrypt(encrypted_text, shift_key)

print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_result}")
