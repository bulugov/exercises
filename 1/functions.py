def count_lines(ignore_whitespace=False):
    # Count the number of non-empty lines in the text file
    file = open("poem.txt", "r")
    totalNonEmpty = 0
    totalEmpty = 0
    if ignore_whitespace == True:
        for line in file:
            # if ignore_whitespace == True:
            if line != "\n":
                nonEmptyLines = line.strip("\n")
                totalNonEmpty = len(nonEmptyLines)
            else:
                totalEmpty += 1

        totalEmpty += totalNonEmpty

        # totalLines2 = len(file.readlines())

    print("Number of lines:", totalEmpty)
    print("Number of lines(non-empty):", totalNonEmpty)
    # Close and reopen the file after each function so one function does not affect the output of the others
    file.close()


def count_words(ignore_whitespace=False):
    # Count the words in the text file
    file = open("poem.txt", "r")
    # data = file.read()
    nonEmptyWords = 0
    for line in file:
        if ignore_whitespace == True:
            line = line.strip("\n")
            words = line.split()
            nonEmptyWords += len(words)

    print("Words(non-empty):", nonEmptyWords)
    print("Words:", nonEmptyWords)
    file.close()


def count_characters(ignore_whitespace=False):
    # Count the characters in the text file
    file = open("poem.txt", "r")
    data = file.read()
    emptyChars = 0
    nonEmptyChars = 0
    for line in data:
        if ignore_whitespace == True:
            line = line.strip("\n")
            nonEmptyChars += len(line)

    emptyChars += len(data)

    print("Chars:", emptyChars)
    print("Chars(non-empty):", nonEmptyChars)


count_lines(True)
count_characters(True)
count_words(True)
