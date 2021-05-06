import string

def fibonacci():
    num1 = 0
    num2 = 1

    num_of_terms = int(input("How far to count to?"))

    if num_of_terms <= 0:
        print("please enter a valid positive integer")

    elif num_of_terms == 1:
            print("Fibonacci sequence of 1 is 1")

    else:
        print("Fibonacci sequence counted to", num_of_terms, ":")

        i = 0

        while i < num_of_terms:
            print(num1)
            next_number = num1 + num2
            num1 = num2
            num2 = next_number
            i = i+1


def dracula():
    min_word_length = 3
    min_word_occurence = 300
    file = open("Dracula.txt", "r")
    word_list = dict()
    for line in file:
        line = line.strip()

        line = line.lower()

        line = line.translate(line.maketrans("", "", string.punctuation))

        words = line.split(" ")

        for word in words:
            if len(word)>min_word_length:
                if word in word_list:
                    word_list[word] = word_list[word] + 1

                else:
                    word_list[word] = 1

    for key in list(word_list.keys()):
        if word_list[key] < min_word_occurence:
            del word_list[key]
        else:
            print(key, ":", word_list[key])


def main():
    #fibonacci()
    dracula()


main()


