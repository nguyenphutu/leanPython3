import os, sys, time
from transpositionCipherEncryption import encryptMessage, decryptMessage

def main():
    inputFile = 'input.txt'
    outputFile = 'output.txt'
    key = 20
    mode = 'encrypt'

    if not os.path.exists(inputFile):
        print('The file %s does not exist. Quitting...' % (inputFile))
        sys.exit()

    if os.path.exists(outputFile):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFile))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFile, 'r')
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (mode.title()))
    startTime = time.time()
    if mode == 'encrypt':
        translated = encryptMessage(key=key, message=content)
    elif mode == 'decrypt':
        translated = decryptMessage(key=key, message=content)

    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (mode.title(), totalTime))

    # Write out the translated message to the output file.

    outputFile = open(outputFile, 'w')
    outputFile.write(translated)
    outputFile.close()

    print('Done %sing %s (%s characters).' % (mode, inputFile, len(content)))
    print('%sed file is %s.' % (mode.title(), outputFile.name))

if __name__ == '__main__':
    main()
