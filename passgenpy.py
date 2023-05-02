import random
import pyperclip

class PasswordGeneratorApp:
    def __init__(self):
        self.root = document.getElementById('root')
        
        self.letters_label = document.createElement('label')
        self.letters_label.textContent = "How many letters would you like in your password?"
        self.root.appendChild(self.letters_label)

        self.letters_entry = document.createElement('input')
        self.root.appendChild(self.letters_entry)

        self.symbols_label = document.createElement('label')
        self.symbols_label.textContent = "How many symbols would you like?"
        self.root.appendChild(self.symbols_label)

        self.symbols_entry = document.createElement('input')
        self.root.appendChild(self.symbols_entry)

        self.numbers_label = document.createElement('label')
        self.numbers_label.textContent = "How many numbers would you like?"
        self.root.appendChild(self.numbers_label)

        self.numbers_entry = document.createElement('input')
        self.root.appendChild(self.numbers_entry)

        self.generate_button = document.createElement('button')
        self.generate_button.textContent = "Generate Password"
        self.generate_button.addEventListener('click', self.generate_password)
        self.root.appendChild(self.generate_button)

        self.password_label = document.createElement('label')
        self.root.appendChild(self.password_label)

        self.copy_button = document.createElement('button')
        self.copy_button.textContent = "Copy Password"
        self.copy_button.addEventListener('click', self.copy_password)
        self.root.appendChild(self.copy_button)

    def generate_password(self):
        nr_letters = int(self.letters_entry.value)
        nr_symbols = int(self.symbols_entry.value)
        nr_numbers = int(self.numbers_entry.value)

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

        self.password_label.textContent = f"Your password is: {password}"
        self.generated_password = password

    def copy_password(self):
        pyperclip.copy(self.generated_password)

app = PasswordGeneratorApp()
