
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


    for key in dict_words:
        print(key, dict_words[key])

count_words()

