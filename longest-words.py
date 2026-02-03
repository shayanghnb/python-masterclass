words = list(input("enter your text: ").split())
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print(f"longest word(s): ")
for word in longest_words:
    print(f"{word}({max_length} letters)")