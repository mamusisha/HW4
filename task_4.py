import string

while True:
    text = input("enter text (letters and digits only): ").strip()
    if text.isalnum():
        break
    print("invalid input! enter only letters and digits.")


if text == text[::-1]:
    print("the text is a palindrome.")
else:
    print("the text is not a palindrome.")

closest_deleting = None
for i in range(len(text)):
     candidate = text[:i] + text[i+1:]
     if candidate == candidate[::-1]:
       closest_deleting = candidate
       break

closest_inserting = None
for i in range(len(text) + 1):
    for c in string.ascii_letters + string.digits:
        candidate = text[:i] + c + text[i:]
        if candidate == candidate[::-1]:
            closest_inserting = candidate
            break
    if closest_inserting:
        break

if closest_inserting:
    print("closest palindrome by inserting one character:", closest_inserting)
if closest_deleting:
    print("closest palindrome by deleting one character:", closest_deleting)
else:
    print("no palindrome can be obtained by a single insertion/deletion.")
