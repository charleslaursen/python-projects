# text_analyzer.py

def analyze_text(text):
    words = text.split()
    word_count = len(words)

    char_count = len(text)

    word_freq = {}
    for word in words:
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1

    print("\nText Analysis:")
    print(f"Total Words: {word_count}")
    print(f"Total Characters: {char_count}")
    print("\nWord Frequency:")

    for word, count in word_freq.items():
        print(f"{word}: {count}")


def main():
    text = input("Enter a sentence or paragraph:\n")
    analyze_text(text)


if __name__ == "__main__":
    main()
