import tkinter as tk
from tkinter import messagebox

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Text --> Morse Code
def encrypt_to_morse(text):
    try:
        return ' '.join(MORSE_CODE_DICT[char] for char in text.upper() if char in MORSE_CODE_DICT)
    except KeyError:
        messagebox.showerror("Error", "Input contains unsupported characters.")
        return ""

# Morse code --> Text
def decrypt_from_morse(morse_code):
    morse_dict_reversed = {v: k for k, v in MORSE_CODE_DICT.items()}
    try:
        return ''.join(morse_dict_reversed[code] for code in morse_code.split() if code in morse_dict_reversed)
    except KeyError:
        messagebox.showerror("Error", "Morse code contains unsupported patterns.")
        return ""

# GUI
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("400x300")

# Input Fields and Labels
label1 = tk.Label(root, text="Input :")
label1.pack(pady=5)
input_field = tk.Entry(root, width=50)
input_field.pack(pady=5)

label2 = tk.Label(root, text="Output :")
label2.pack(pady=5)
output_field = tk.Entry(root, width=50, state='readonly')
output_field.pack(pady=5)

# Button Functions
def encrypt():
    text = input_field.get()
    if text.strip():
        morse_code = encrypt_to_morse(text)
        output_field.config(state='normal')
        output_field.delete(0, tk.END)
        output_field.insert(0, morse_code)
        output_field.config(state='readonly')
    else:
        messagebox.showwarning("Warning", "Please enter text to encrypt!")

def decrypt():
    morse_code = input_field.get()
    if morse_code.strip():
        text = decrypt_from_morse(morse_code)
        output_field.config(state='normal')
        output_field.delete(0, tk.END)
        output_field.insert(0, text)
        output_field.config(state='readonly')
    else:
        messagebox.showwarning("Warning", "Please enter Morse code to decrypt!")

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=10)

root.mainloop()
