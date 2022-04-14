def countLines():
    file = open("poem.txt", "r")
    for line in file:
        if line != "\n":
            nonEmptyLines = line.strip("\n")

    totalLines = len(nonEmptyLines)

    print("Lines:", totalLines)
    file.close()


def countWords():
    file = open("poem.txt", "r")
    totalWords = 0
    for line in file:
        line = line.strip("\n")
        words = line.split()
        totalWords += len(words)

    print("Words:", totalWords)
    file.close()


def countChars():
    file = open("poem.txt", "r")
    totalChars = 0
    for line in file:
        line = line.strip("\n")
        totalChars += len(line)
    print("Chars:", totalChars)
