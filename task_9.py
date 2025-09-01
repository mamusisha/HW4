text = input("enter text: ")
words = text.lower().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
max_count = max(counts.values())

most_frequent = []
for w, c in counts.items():
    if c == max_count:
        most_frequent.append(w)

print("frequent word(s):", most_frequent)
print("repeating count:", max_count)