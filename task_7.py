text = input("enter text to filter: ")

filtered_text = ""
for char in text:
    if char.isalpha() or char == ' ':
        filtered_text += char

cleaned_text = ""
previous_was_space = False
for char in filtered_text:
    if char == ' ':
        if not previous_was_space:
            cleaned_text += char
        previous_was_space = True
    else:
        cleaned_text += char
        previous_was_space = False

print(f"filtered text: {cleaned_text}")