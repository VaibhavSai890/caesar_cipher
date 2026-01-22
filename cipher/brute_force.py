from cipher.caesar import caesar_cipher

def brute_force_decrypt(text):
    results = ""
    for shift in range(26):
        decrypted = caesar_cipher(text, -shift)
        results += f"Shift {shift}: {decrypted}\n"
    return results
