import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string
import pyperclip

def generate_password():
    # Ask for password length
    password_length = simpledialog.askinteger("Password Length", "Enter the password length:")
    
    if password_length is not None:
        use_lowercase = tk.BooleanVar()
        use_uppercase = tk.BooleanVar()
        use_digits = tk.BooleanVar()
        use_special_chars = tk.BooleanVar()
        
        # Options dialog window
        options_window = tk.Toplevel(root)
        options_window.title("Password Options")
        
        tk.Label(options_window, text="Select password options:").pack()
        
        tk.Checkbutton(options_window, text="Lowercase Letters", variable=use_lowercase).pack()
        tk.Checkbutton(options_window, text="Uppercase Letters", variable=use_uppercase).pack()
        tk.Checkbutton(options_window, text="Digits", variable=use_digits).pack()
        tk.Checkbutton(options_window, text="Special Characters", variable=use_special_chars).pack()
        
        def generate():
            chars = ""
            if use_lowercase.get():
                chars += string.ascii_lowercase
            if use_uppercase.get():
                chars += string.ascii_uppercase
            if use_digits.get():
                chars += string.digits
            if use_special_chars.get():
                chars += string.punctuation
            
            if chars:
                password = ''.join(random.choice(chars) for _ in range(password_length))
                # Copy the password to the clipboard
                pyperclip.copy(password)
                messagebox.showinfo("Generated Password", password + "\n\nThe password has been copied to the clipboard.")
            else:
                messagebox.showerror("Error", "Select at least one option.")
        
        tk.Button(options_window, text="Generate Password", command=generate).pack()
    else:
        messagebox.showerror("Error", "Please enter a valid password length.")

root = tk.Tk()
root.title("Password Generator")

welcome_label = tk.Label(root, text="Welcome to the password generator!", font=("Arial", 16))
welcome_label.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

root.mainloop()
