# Makes the wordPatterns.py File
# Creates wordPatterns.py based on the words in our dictionary
# text file, dictionary.txt. (Download this file from
# http://invpy.com/dictionary.txt)

import pprint


def getWordPattern(word):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])

    return '.'.join(wordPattern)


def main():
    allPatterns = {}
    file_word = open('dictionary.txt')
    wordList = file_word.read().split('\n')
    file_word.close()

    for word in wordList:
        # Get the pattern for each string in wordList.
        pattern = getWordPattern(word)
        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    file_word_pattern = open('wordPatterns.py', 'w')
    file_word_pattern.write('allPatterns = ')
    file_word_pattern.write(pprint.pformat(allPatterns))
    file_word_pattern.close()


if __name__ == '__main__':
    main()
