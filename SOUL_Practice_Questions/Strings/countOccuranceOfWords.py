def countOccurancesOfWords(input_string):

    word_dict = {}

    words = input_string.split(" ")

    print(words)

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

input_string = input("Enter a string: ")

wordCount = countOccurancesOfWords(input_string)

for word,frequency in wordCount.items():
    print(f"{word} : {frequency}")

