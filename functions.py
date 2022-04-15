def count_lines(ignore_whitespace=False):
    # Count the number of non-empty lines in the text file
    totalLines = 0
    with open("poem.txt", "r") as file:
        for line in file:
            if ignore_whitespace == True:
                if line != "\n":
                    nonEmptyLines = line.strip("\n")
                    totalLines = len(nonEmptyLines)
            else:
                totalLines += 1

    if ignore_whitespace == True:
        print("Number of lines (non-empty):", totalLines)
    else:
        print("Number of lines:", totalLines)


def count_words(ignore_whitespace=False):
    # Count the words in the text file
    totalWords = 0
    with open("poem.txt", "r") as file:
        for line in file:
            if ignore_whitespace == True:
                line = line.strip("\n")
                words = line.split()
                totalWords += len(words)
            else:
                # line = line.strip("\n")
                words = line.split()
                totalWords += len(words)

    if ignore_whitespace == True:
        print("Number of words (non-empty):", totalWords)
    else:
        print("Number of words:", totalWords)


def count_characters(ignore_whitespace=False):
    # Count the characters in the text file
    totalChars = 0
    with open("poem.txt", "r") as file:
        for line in file:
            if ignore_whitespace == True:
                line = line.strip("\n")
                totalChars += len(line)
            else:
                totalChars += len(line)

    if ignore_whitespace == True:
        print("Number of chars (non-empty):", totalChars)
    else:
        print("Number of characters:", totalChars)
