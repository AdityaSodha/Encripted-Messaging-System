import tkinter as tk
from tkinter import messagebox
from mapping import custom_mapping

def encode_text(text, mapping):
    encoded_chars = []
    for char in text:
        if char in mapping:
            encoded_chars.append(mapping[char])
        else:
            encoded_chars.append(char)  
    return ''.join(encoded_chars)
 
def decode_text(encoded_text, mapping):
    reverse_mapping = {value: key for key, value in mapping.items()}
    decoded_text = []
    encoded_sequence = ""
    
    for char in encoded_text:
        encoded_sequence += char
        if encoded_sequence in reverse_mapping:
            decoded_text.append(reverse_mapping[encoded_sequence])
            encoded_sequence = ""
    
    return ''.join(decoded_text)

def on_encode():
    text_to_encode = encode_entry.get()
    if not text_to_encode:
        messagebox.showerror("Input Error", "Please enter text to encode.")
        return
    encoded_text = encode_text(text_to_encode, custom_mapping)
    encoded_text_var.set(encoded_text)

def on_decode():
    encoded_text_to_decode = decode_entry.get()
    if not encoded_text_to_decode:
        messagebox.showerror("Input Error", "Please enter encoded text to decode.")
        return
    decoded_text = decode_text(encoded_text_to_decode, custom_mapping)
    decoded_text_var.set(decoded_text)


root = tk.Tk()
root.title("Text Encoder and Decoder")


tk.Label(root, text="Enter text to encode:").grid(row=0, column=0, padx=10, pady=10)
encode_entry = tk.Entry(root, width=50)
encode_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Encode", command=on_encode).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Encoded Text:").grid(row=1, column=0, padx=10, pady=10)
encoded_text_var = tk.StringVar()
tk.Entry(root, textvariable=encoded_text_var, state='readonly', width=50).grid(row=1, column=1, padx=10, pady=10)


tk.Label(root, text="Enter encoded text to decode:").grid(row=2, column=0, padx=10, pady=10)
decode_entry = tk.Entry(root, width=50)
decode_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Decode", command=on_decode).grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Decoded Text:").grid(row=3, column=0, padx=10, pady=10)
decoded_text_var = tk.StringVar()
tk.Entry(root, textvariable=decoded_text_var, state='readonly', width=50).grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
