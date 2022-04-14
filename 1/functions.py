def countLines():
    # Count the number of non-empty lines in the text file
    file = open("poem.txt", "r")
    for line in file:
        if line != "\n":
            nonEmptyLines = line.strip("\n")

    totalLines = len(nonEmptyLines)

    print("Lines:", totalLines)
    # Close the file after each function so one function does not affect the output of the others
    file.close()


def countWords():
    # Count the words in the text file
    file = open("poem.txt", "r")
    totalWords = 0
    for line in file:
        line = line.strip("\n")
        words = line.split()
        totalWords += len(words)

    print("Words:", totalWords)
    file.close()


def countChars():
    # Count the characters in the text file
    file = open("poem.txt", "r")
    totalChars = 0
    for line in file:
        line = line.strip("\n")
        totalChars += len(line)
    print("Chars:", totalChars)
