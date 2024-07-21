import re


def single_root_words(root_word, *other_words):
    same_words = []
    lower_word = root_word.lower()
    for word in other_words:
        if lower_word in word.lower() or word.lower() in lower_word:
           same_words.append(word)
    return list(same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)