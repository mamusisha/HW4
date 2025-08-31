import string

while True:
    user_input = input("enter the length of Fibonacci sequence you want: ")

    if user_input.isdigit():
        n = int(user_input)
        break
    else:
        symbols_in = False
        strange_in = False
        characters_in = False
        for ch in user_input:
            if ch in string.ascii_letters:
                characters_in = True
            elif ch in string.punctuation:
                symbols_in = True
            elif ch in string.digits:
                pass
            else:
                strange_in = True
        if symbols_in: print("you entered symbols")
        if strange_in: print("you entered strange characters")
        if characters_in: print("you entered characters")

fibonacci_list = []
if n >= 1:
    fibonacci_list.append(0)
if n >= 2:
    fibonacci_list.append(1)
for i in range(2, n):
    fibonacci_list.append( fibonacci_list[i - 1] + fibonacci_list[i - 2])
print(f"Fibonacci sequence with {n} numbers:")
print(fibonacci_list)
