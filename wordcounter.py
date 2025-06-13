print(" Word Counter")


text = input("Enter a sentence  here: ")
words = text.split()


print("\nTotal number of words:", len(words))
counts = {}
for w in words:
    w = w.lower()  
    if w in counts:
        counts[w] += 1  
    else:
        counts[w] = 1   

print("\nWord counts:")
for word in counts:
    print(word + ":", counts[word])

most_word = ""
most_count = 0

for word in counts:
    if counts[word] > most_count:
        most_word = word
        most_count = counts[word]

print("\nMost frequent word:")
print("'" + most_word + "' occurs", most_count, "times")
