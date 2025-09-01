import random

def is_number(s):
    if s.count('.') <= 1:
        if s.replace('.', '', 1).lstrip('-').isdigit():
            return True
    return False

while True:
    user_input = input("enter numbers separated by spaces: ").strip()
    parts = user_input.split()

    if parts and all(is_number(part) for part in parts):
        numbers = [float(part) for part in parts]
        break
    else:
        print("invalid input!")

print("\nsorting options:")
print("1. ascending (smallest to largest)")
print("2. descending (largest to smallest)")
print("3. random order")
print("4. keep only unique values")

while True:
    choice = input("choose sorting option (1-4): ")
    if choice in ['1', '2', '3', '4']:
        break
    else:
        print("invalid choice! Please enter 1, 2, 3, or 4.")

if choice == '1':
    sorted_list = sorted(numbers)
    print(f"sorted in ascending order: {sorted_list}")

elif choice == '2':
    sorted_list = sorted(numbers)
    reversed_list = sorted_list[::-1]
    print(f"Sorted in descending order: {reversed_list}")

elif choice == '3':
    sorted_list = numbers.copy()
    random.shuffle(sorted_list)
    print(f"randomly ordered: {sorted_list}")

elif choice == '4':
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    unique_sorted = sorted(unique_list)
    print(f"unique values only (sorted): {unique_sorted}")
