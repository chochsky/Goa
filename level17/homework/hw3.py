def filter_vowels(text):
    vowels = "aeiouAEIOUაეიოუ"
    return ''.join([ch for ch in text if ch in vowels])
