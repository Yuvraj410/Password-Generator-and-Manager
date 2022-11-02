# Sample space for password generation
S_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
C_letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Password Dictionary
PDict = {}

#PasswordGenerator
import random

class PasswordGenerator:
    def generate(self, site, nr_S_letters, nr_C_letters, nr_symbols, nr_numbers):
        password_list = []
        for char in range(1, nr_S_letters + 1):
            password_list.append(random.choice(S_letters))
        for char in range(1, nr_C_letters + 1):
            password_list.append(random.choice(C_letters))
        for symbol in range(1, nr_symbols + 1):
            password_list.append(random.choice(symbols))
        for num in range(1, nr_numbers + 1):
            password_list.append(random.choice(numbers))

        # shuffling the password
        random.shuffle(password_list)
        rpassword = ""
        for char in password_list:
            rpassword += char

        #adding password to dict
        # check if key not in dict
        if site not in PDict:
            PDict[site] = rpassword

        # OUTPUT
        print("\n")
        print(f'The generated password is : {rpassword}')

    def load_password_dict(self):
        print(PDict)

#Password Manager
from cryptography.fernet import  Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site,password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]

#main function
print("Welcome to the Python Password Generator!")

password = PDict
pg = PasswordGenerator()
pm = PasswordManager()

print("""What do you want to do?
    (1) Create a new random password and add it to the Password Dictionary
    (2) Create a new key 
    (3) Load an existing key
    (4) Create new password file for PM
    (5) Load existing password file
    (6) Add a new password
    (7) Get a password
    (8) Get password dictionary
    (9) Quit
    """)
done = False

    while not done:
        choice=input("Enter your choice: ")
        if choice == "1":
            site = input("Enter Site's name: ")
            nr_S_letters = int(input("How many SMALL letters would you like in your password?\n"))
            nr_C_letters = int(input("How many CAPITAL letters would you like in your password?\n"))
            nr_symbols = int(input("How many symbols would you like?\n"))
            nr_numbers = int(input("How many numbers would you like?\n"))
            pg.generate(site, nr_S_letters, nr_C_letters, nr_symbols, nr_numbers)
        elif choice == "2":
            path = input("Enter path")
            pm.create_key(path)
        elif choice == "3":
            path = input("Enter path")
            pm.load_key(path)
        elif choice == "4":
            path = input("Enter path")
            pm.create_password_file(path, password)
        elif choice == "5":
            path = input("Enter path")
            pm.load_password_file(path)
        elif choice == "6":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "7":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "8":
            pg.load_password_dict()
        elif choice == "9":
            done = True
        else:
            print("Invalid choice!!")
