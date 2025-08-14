def replace_vowels_with_exclamation(sentence):
    vowels = "aeiouAEIOU"
    return ''.join('!' if char in vowels else char for char in sentence)
