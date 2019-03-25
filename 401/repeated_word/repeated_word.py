from hashtable.hashtable import Hashtable
import re


def first_repeated_word(string):
    string = re.sub(r'[^A-Za-z0-9 ]', '', string)
    string = string.lower()
    words = string.split(' ')
    ht = Hashtable()
    for word in words:
        if ht.contains(word):
            return word
        else:
            ht.add(word, None)
    return None
