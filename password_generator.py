import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many letters do you wanna have?\n"))
num_numbers = int(input("How many numbers do you wanna have?\n"))
num_symbols = int(input("How many symbols do you wanna have?\n"))

password = []

if  num_letters < 0 or num_numbers < 0 or num_symbols < 0:
   print("Please enter non-negative numbers for the quantities.")
   exit()

if num_letters != 0:
    for l in range(1, num_letters + 1):
      password.append(random.choice(letters))

if num_numbers != 0:
   for n in range(1, num_numbers + 1):
      password.append(random.choice(numbers))

if num_symbols != 0: 
   for s in range(1, num_symbols + 1):
      password.append(random.choice(symbols))

random.shuffle(password)

randomised_password = ""

for char in password:
    randomised_password += char

print(f"Your password is {randomised_password}")