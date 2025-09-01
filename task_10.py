import string

text = input("enter text: ")
words = text.split()
counts = {}
for w in words:
    clean_w = w.strip(string.punctuation)
    counts[clean_w] = len(clean_w)
print(counts)