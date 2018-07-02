
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
import operator
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

    #1
    # for item in sorted(cnt):
    #     print("{} : {}".format(item, cnt[item]))

    #2
    # sort_cnt = sorted(cnt.items(),key=lambda kv: kv[1])
    # for item in sort_cnt:
    #     #print("{} : {}".format(item[0], item[1]))

    #3
    reverse_sort_cnt = []
    sort_cnt = sorted(cnt.items(),key=lambda kv: kv[1])

    for i in range(len(sort_cnt)):
        reverse_sort_cnt.append(sort_cnt[len(sort_cnt)-1-i])

    print (reverse_sort_cnt)

    for tupl in reverse_sort_cnt:
        if tupl[1] == ""
    # for item in sorted(reverse_sort_cnt):

    #     print("{} : {}".format(item, reverse_sort_cnt[item]))


        #print ("{} : {}".format(sort_cnt[len(sort_cnt)-1-i][0], sort_cnt[len(sort_cnt)-1-i][1]))

count_words_w_count()
