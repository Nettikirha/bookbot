def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letters = {}
    text = text.lower()
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sorter(characters):
    filtered = {k: v for k, v in characters.items() if k.isalpha() and len(k) == 1}
    return [{k: v} for k, v in sorted(filtered.items(), key=lambda x: x[1], reverse=True)]

 