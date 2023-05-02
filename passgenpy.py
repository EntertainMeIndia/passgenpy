import random
import tkinter as tk
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("PyPassword Generator")

        self.letters_label = tk.Label(master, text="How many letters would you like in your password?")
        self.letters_label.pack()

        self.letters_entry = tk.Entry(master)
        self.letters_entry.pack()

        self.symbols_label = tk.Label(master, text="How many symbols would you like?")
        self.symbols_label.pack()

        self.symbols_entry = tk.Entry(master)
        self.symbols_entry.pack()

        self.numbers_label = tk.Label(master, text="How many numbers would you like?")
        self.numbers_label.pack()

        self.numbers_entry = tk.Entry(master)
        self.numbers_entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="")
        self.password_label.pack()

        self.copy_button = tk.Button(master, text="Copy Password", command=self.copy_password)
        self.copy_button.pack()

    def generate_password(self):
        nr_letters = int(self.letters_entry.get())
        nr_symbols = int(self.symbols_entry.get())
        nr_numbers = int(self.numbers_entry.get())

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = ['']
        for char in range(1, nr_letters + 1):
            random_choice = random.choice(letters)
            password_list += random_choice
            random.shuffle(password_list)

        for char in range(1, nr_symbols + 1):
            random_choice = random.choice(symbols)
            password_list += random_choice
            random.shuffle(password_list)

        for char in range(1, nr_numbers + 1):
            random_choice = random.choice(numbers)
            password_list += random_choice
            random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char

        self.password_label.config(text=f"Your password is: {password}")
        self.generated_password = password

    def copy_password(self):
        pyperclip.copy(self.generated_password)

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
