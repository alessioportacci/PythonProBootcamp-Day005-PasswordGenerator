import random

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the PyPassword Generator!\n")
letters_number = int(
  input("How many letters would you like in your password?\n"))
symbols_number = int(input("How many symbols?\n"))
numbers_number = int(input("How many numbers?\n"))

for n_letter in range(0, letters_number):
  password += random.choice(letters)
for n_symbols in range(0, symbols_number):
  password += random.choices(symbols)
for n_numbers in range(0, numbers_number):
  password += random.choices(numbers)

random.shuffle(password)
print(''.join(password))