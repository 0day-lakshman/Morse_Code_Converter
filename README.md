# Morse_Code_Converter
The code you provided is a Python script that implements a Morse code converter with a graphical user interface (GUI) built using the tkinter library.

Here's a breakdown of the code:

1. **Morse Code Dictionary:**
   - A dictionary named `MORSE_CODE_DICT` is defined, mapping each English letter and some symbols to their corresponding Morse code representation (e.g., 'A' -> '.-').

2. **Encryption and Decryption Functions:**
   - `encrypt_to_morse(text)`: This function takes a text string as input and encrypts it to Morse code. It iterates over each character in the text, converts it to uppercase, and looks up its corresponding Morse code in the dictionary. If a character is not found in the dictionary, a KeyError is raised.
   - `decrypt_from_morse(morse_code)`: This function takes a Morse code string as input and decrypts it to text. It splits the Morse code string into individual codes (separated by spaces) and iterates over them. For each code, it looks up the corresponding character in a reversed dictionary (created by inverting the `MORSE_CODE_DICT`). If a code is not found in the dictionary, a KeyError is raised.

3. **GUI Implementation:**
   - The code uses tkinter to create a GUI window titled "Morse Code Converter".
   - It defines labels and entry fields for input and output text.
   - The `encrypt` and `decrypt` functions are bound to buttons that trigger the respective encryption or decryption functionality when clicked.
   - These functions handle user input, perform encryption or decryption using the defined functions, and update the output field accordingly.
   - Error handling is implemented using message boxes to warn the user about empty input or unsupported characters/codes.

Overall, this code provides a user-friendly interface for converting text to Morse code and vice versa.
