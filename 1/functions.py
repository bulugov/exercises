def count_lines(ignore_whitespace):
    # Count the number of non-empty lines in the text file
    file = open("poem.txt", "r")
    for line in file:
        if line != "\n":
            nonEmptyLines = line.strip("\n")

    totalLines = len(nonEmptyLines)

    print("Lines:", totalLines)
    # Close and reopen the file after each function so one function does not affect the output of the others
    file.close()


def count_words(ignore_whitespace):
    # Count the words in the text file
    file = open("poem.txt", "r")
    totalWords = 0
    for line in file:
        line = line.strip("\n")
        words = line.split()
        totalWords += len(words)

    print("Words:", totalWords)
    file.close()


def count_characters(ignore_whitespace):
    # Count the characters in the text file
    file = open("poem.txt", "r")
    totalChars = 0
    for line in file:
        line = line.strip("\n")
        totalChars += len(line)
    print("Chars:", totalChars)
