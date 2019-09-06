def count_words_in_string(sent):
    sent = sent.split()
    summary = {w: sent.count(w) for w in sent}
    with open('Count words.txt', 'w') as file:
        for word, val in summary.items():
            file.write(f'{word} = {val} ' + '\n')
        # print(summary, file=file)


sentence = 'I do not know what should i write ? Writing this in text file is a good idea.' \
           ' oh i remember i should repeat some words, actually repeating is also good practice' \
           ' see how i repeat repeat several times'
count_words_in_string(sentence)
