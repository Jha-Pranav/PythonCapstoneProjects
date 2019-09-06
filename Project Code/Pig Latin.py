vowel = ('a', 'e', 'i', 'o', 'u')


def pig_latin(word):
    word = word.lower()
    if word[0] in vowel:
        return word + 'way'
    else:
        cluster = ''
        rest = ''
        loop = word[0] not in vowel
        for i in word:
            if i not in vowel and loop:
                cluster += i
            else:
                loop = False
                rest += i
    return rest + cluster + 'ay'


print(pig_latin('pig'))
print(pig_latin('latin'))
print(pig_latin('stupid'))
print(pig_latin('honest'))
print(pig_latin('omelet'))
