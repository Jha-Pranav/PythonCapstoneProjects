def count_vowel(sent):
    """
    Using list and dictionary comprehension
    """
    f = [s for s in sent if s in ('a', 'e', 'i', 'o', 'u')]
    return {c: f.count(c) for c in f}


sentence = 'Hello! there, how do you do?'
print(count_vowel(sentence))
