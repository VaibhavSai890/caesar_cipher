from cipher.caesar import caesar_cipher

def process_file(filepath, shift):
    with open(filepath, 'r') as file:
        content = file.read()

    encrypted_content = caesar_cipher(content, shift)

    with open(filepath, 'w') as file:
        file.write(encrypted_content)

    return "File processed successfully."
