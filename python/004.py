def spin_words(sentence):
    if '' in sentence:
        word = sentence.split()
        for k, v in enumerate(word):
            if len(v) >= 5:
                word[k] = v[::-1]
    else:
        word = sentence[::-1]

    return ' '.join(word)


print(spin_words("Hey fellow warriors"))