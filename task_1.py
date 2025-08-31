import random
import string

while True:
    length = input("enter password length: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("invalid password length!")
        continue

#set to save options
character_sets = []
options = {
    "lowercase letters": string.ascii_lowercase,
    "uppercase letters": string.ascii_uppercase,
    "numbers": string.digits,
    "symbols": string.punctuation
}
for label, chars in options.items():
    choice = input(f"include {label}? (y/n): ").lower()
    if choice == 'y':
        character_sets.append(chars)

character_sets = ''.join(character_sets)

password = ""
for i in range(length):
    password += random.choice(character_sets)
print("generated password: ", password)