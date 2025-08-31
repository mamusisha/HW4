import string

password = input("enter password to evaluate: ")
score = 0

length = len(password)
if length >= 20:
    score += 4
elif length >= 15:
    score += 3
elif length >= 10:
    score += 2
elif length >= 5:
    score += 1
else:
    print("your password is too short")

has_lowercase = False
has_uppercase = False
has_digits = False
has_symbols = False
for c in password:
    if c in string.ascii_lowercase:
        has_lowercase = True
    elif c in string.ascii_uppercase:
        has_uppercase = True
    elif c in string.digits:
        has_digits = True
    elif c in string.punctuation:
        has_symbols = True

variety_score = sum([has_lowercase, has_uppercase, has_digits, has_symbols])

if variety_score <= 2:
    print("you need to use different character sets")
score += variety_score


char_count = {}
for char in password:
    char_count[char] = char_count.get(char, 0) + 1
max_repetition = max(char_count.values())
if max_repetition >= 3:
    print("excessive repetition!!")
elif max_repetition >= 2:
    score += 1
else:
    score += 2


if score >= 8:
    strength = "Strong"
elif score >= 5:
    strength = "Medium"
else:
    strength = "Weak"

print(f"your password is {strength}, score is {score}")