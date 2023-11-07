import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    # Pytanie o długość hasła
    password_length = simpledialog.askinteger("Długość hasła", "Podaj długość hasła:")
    
    if password_length is not None:
        use_lowercase = tk.BooleanVar()
        use_uppercase = tk.BooleanVar()
        use_digits = tk.BooleanVar()
        use_special_chars = tk.BooleanVar()
        
        # Okno dialogowe z opcjami
        options_window = tk.Toplevel(root)
        options_window.title("Opcje hasła")
        
        tk.Label(options_window, text="Wybierz opcje hasła:").pack()
        
        tk.Checkbutton(options_window, text="Małe litery", variable=use_lowercase).pack()
        tk.Checkbutton(options_window, text="Wielkie litery", variable=use_uppercase).pack()
        tk.Checkbutton(options_window, text="Cyfry", variable=use_digits).pack()
        tk.Checkbutton(options_window, text="Znaki specjalne", variable=use_special_chars).pack()
        
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
                # Kopiowanie hasła do schowka
                pyperclip.copy(password)
                messagebox.showinfo("Wygenerowane hasło", password + "\n\nHasło zostało skopiowane do schowka.")
            else:
                messagebox.showerror("Błąd", "Wybierz co najmniej jedną opcję.")
        
        tk.Button(options_window, text="Generuj hasło", command=generate).pack()
    else:
        messagebox.showerror("Błąd", "Podaj prawidłową długość hasła.")

root = tk.Tk()
root.title("Generator hasła")

welcome_label = tk.Label(root, text="Witaj w generatorze haseł!", font=("Arial", 16))
welcome_label.pack()

generate_button = tk.Button(root, text="Generuj hasło", command=generate_password)
generate_button.pack()

root.mainloop()
