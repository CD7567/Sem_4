a, b = int(input()), int(input())

word, word_counter, len_counter = input(), 0, 0

while word != '0':
    if word_counter == 0:
        print(word, end = '')
    else:
        if (len_counter + len(word) < a and word_counter < b):
            len_counter += 1
            print(' ' + word, end = '')
        else:
            word_counter = 0
            len_counter = 0
            print()
            continue
    word_counter += 1
    len_counter += len(word)
    word = input()