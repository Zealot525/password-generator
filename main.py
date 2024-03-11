#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '~', '`', '^', '_']

print("Welcome to your very own Pysword Generator!")
nr_letters= int(input("What is the total amount of characters you would like in your password?\n")) 
nr_symbols = int(input(f"Out of the {nr_letters} characters, how many symbols would you like to include?\n"))
nr_numbers = int(input(f"How many out of the remaining {nr_letters - nr_symbols} would you like to be numbers?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# easy_password = random.choices(letters)
# for letter in range(0, nr_letters - 1): 
#   easy_password += random.choices(letters)
# for symbol in range(0, nr_symbols):
#   easy_password += random.choices(symbols)
# for number in range(0, nr_numbers):
#   easy_password += random.choices(numbers)
# print(''.join(easy_password))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = random.choices(letters)
for letter in range(0, nr_letters - nr_symbols - nr_numbers - 1): 
  hard_password += random.choices(letters)
for symbol in range(0, nr_symbols):
  hard_password += random.choices(symbols)
for number in range(0, nr_numbers):
  hard_password += random.choices(numbers)

shuffled_password = random.sample(hard_password, len(hard_password))
print(f"This could be your password {''.join(shuffled_password)}")