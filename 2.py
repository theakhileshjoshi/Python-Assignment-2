word = input("Enter a word.")
print("Output", end=":")
for i in reversed(range(len(word))):
    print(word[i], end="")
