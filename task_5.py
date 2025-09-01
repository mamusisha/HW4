while True:
    name = input("enter your name: ").strip()
    if " " in name:
        print("error: please enter only one word!")
    elif not name.isalpha():
        print("error: enter only letters!")
    else:
        break

u_endings = {'u': ["uka", "ushka", "uki", "usha", "ushki"],
    'i':["usa", "usha", "una", "ikuna", "ishka"],
    'e':["uka", "eko", "esha", "eshka", "ekuna"],
    'a':["akuna", "ushka", "uka", "uli", "iko"],
    'o': ["okuna", "usha", "uka", "iko", "una"]}

for key, value in u_endings.items():
    if name[-1] == key:
        for word in value:
            print(f"{name[:-1]}{word}")
