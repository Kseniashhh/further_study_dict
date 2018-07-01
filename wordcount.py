
import sys
def count_words():
    filename = open(sys.argv[1])
    dict_words = {}
    for line in filename:
        line = line.rstrip()
        line = line.split(" ")
        for word in line:
            for letter in word:
                if not letter.isalpha():
                    word = word.replace(letter,"")
            word=word.lower()
            dict_words[word] = dict_words.get(word,0) + 1


    for key, value in dict_words.items():
        print("{} : {}".format(key, value))

#count_words()



import sys
import collections

def count_words_w_count():
    filename = open(sys.argv[1])
    full_text= []
    for line in filename:
        line = line.rstrip()
        line = line.split(" ")
        full_text.extend(line)
    for i in range(len(full_text)):
        for letter in full_text[i]:
            if not letter.isalpha():
                full_text[i] = full_text[i].replace(letter,"")
        full_text[i]=full_text[i].lower()
    cnt = collections.Counter(full_text)

    for key, value in cnt.items():
        print("{} : {}".format(key, value))

count_words_w_count()
