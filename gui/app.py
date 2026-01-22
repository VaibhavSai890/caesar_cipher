import tkinter as tk
from tkinter import filedialog, messagebox

from cipher.caesar import caesar_cipher
from cipher.brute_force import brute_force_decrypt
from cipher.frequency_analysis import detect_shift
from file_ops.file_encrypt import process_file


def launch_app():
    root = tk.Tk()
    root.title("Caesar Cipher Tool")
    root.geometry("520x520")

    # Input Text
    tk.Label(root, text="Enter Text").pack()
    text_entry = tk.Entry(root, width=60)
    text_entry.pack(pady=5)

    # Shift
    tk.Label(root, text="Shift Value").pack()
    shift_entry = tk.Entry(root)
    shift_entry.pack(pady=5)

    # Output Area
    output = tk.Text(root, height=12, width=60)
    output.pack(pady=10)

    def encrypt():
        output.delete(1.0, tk.END)
        shift = int(shift_entry.get())
        output.insert(tk.END, caesar_cipher(text_entry.get(), shift))

    def decrypt():
        output.delete(1.0, tk.END)
        shift = int(shift_entry.get())
        output.insert(tk.END, caesar_cipher(text_entry.get(), -shift))

    def brute_force():
        output.delete(1.0, tk.END)
        output.insert(tk.END, brute_force_decrypt(text_entry.get()))

    def auto_detect():
        output.delete(1.0, tk.END)
        shift = detect_shift(text_entry.get())
        decrypted = caesar_cipher(text_entry.get(), -shift)
        output.insert(tk.END, f"Detected Shift: {shift}\n\n{decrypted}")

    def encrypt_file():
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filepath:
            shift = int(shift_entry.get())
            message = process_file(filepath, shift)
            messagebox.showinfo("Success", message)

    # Buttons
    tk.Button(root, text="Encrypt", command=encrypt, width=20).pack(pady=2)
    tk.Button(root, text="Decrypt", command=decrypt, width=20).pack(pady=2)
    tk.Button(root, text="Brute Force", command=brute_force, width=20).pack(pady=2)
    tk.Button(root, text="Auto Detect Shift", command=auto_detect, width=20).pack(pady=2)
    tk.Button(root, text="Encrypt File", command=encrypt_file, width=20).pack(pady=2)

    root.mainloop()
