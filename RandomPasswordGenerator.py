# Password Generator Project
# noinspection PyUnresolvedReferences
import random

# Sample space for password generation
S_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
C_letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Getting user input for password generation
print("Welcome to the Python Password Generator!")
nr_S_letters = int(input("How many SMALL letters would you like in your password?\n"))
nr_C_letters = int(input("How many CAPITAL letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Random password generation package
# generating password as per user input
password_list = []
for char in range(1, nr_S_letters+1):
    password_list.append(random.choice(S_letters))
for char in range(1, nr_C_letters+1):
    password_list.append(random.choice(C_letters))
for symbol in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
for num in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

# shuffling the password
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

# output
print("\n")
print(f'The generated password is : {password}')

# Fernet module is imported from the
# cryptography package
from cryptography.fernet import Fernet

# key is generated
key = Fernet.generate_key()

# value of key is assigned to a variable
f = Fernet(key)

# the plaintext is converted to ciphertext
token = f.encrypt(password.encode())

# display the ciphertext
print(f'The encrypted password is : {token}')

# decrypting the ciphertext
d = f.decrypt(token)

# display the plaintext
print(f'The decrypted password is : {d.decode()}')