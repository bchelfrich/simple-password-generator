import random
import os
os.system('cls')

upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = upperCase.lower()
digits = '0123456789'
symbols = '!@#$%^&*_;:'

upper , lower , nums , syms = True , True , True , True

all = ''
print("([Y] for yes | [N] for no)")

answer = input("Include uppercase letters? ").lower().strip()
if answer == 'n':
    upper = False
else:
    all += upperCase

answer = input("Include lowercase letters? ").lower().strip()
if answer == 'n':
    lower = False
else:
    all += lowerCase

answer = input("Include digits? ").lower().strip()
if answer == 'n':
    digits = False
else:
    all += digits

answer = input("Include symbols? ").lower().strip()
if answer == 'n':
    syms = False
else:
    all += symbols

number = input("How many passwords? ")
number = int(number)

length = input("Enter password length: ")
length = int(length)

for p in range(number):
    for c in range(length):
        password = "".join(random.sample(all, length))
    print(password)
