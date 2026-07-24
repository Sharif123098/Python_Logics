def word_frequency(text):
    clean_text = ""
    for char in text:
        if char.isalpha() or char == " ":
            clean_text += char
        else:
            clean_text += " "

    words = clean_text.lower().split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    print("Top 3 words:")
    for i in range(3):
        word, count = sorted_words[i]
        print(f"{word} — {count} times")


text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

word_frequency(text)
