filename = open("test.txt")

def count_words(filename):
    dict_words = {}
    for line in filename:
        line = line.rstrip()
        line = line.split(" ")
        for word in line:
            dict_words[word] = dict_words.get(word,0) + 1


    for key in dict_words:
        print(key, dict_words[key])
