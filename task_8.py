while True:
    user_input = input("enter positive integers separated by spaces: ").strip()
    parts = user_input.split()

    if parts and all(part.isdigit() for part in parts):
        numbers = [int(part) for part in parts]
        break
    else:
        print("invalid input!")

pyramid = [numbers]
current_row = numbers

while len(current_row) > 1:
    next_row = []
    for i in range(len(current_row) - 1):
        sum_adjacent = current_row[i] + current_row[i + 1]
        next_row.append(sum_adjacent)
    pyramid.append(next_row)
    current_row = next_row

for row in pyramid:
    for element in row:
        print(element, end=" ")
    print()

