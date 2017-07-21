import pyperclip, sys, random

#LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXY Z[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, ' \
                'and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, ' \
                'he is offered something which affords a reason for acting in accordance to his instincts, ' \
                'he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    #myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myKey = r"""/{9@6hUf:q?_)^eTi|W1,NLD7xk(-SF>Iz0E=d;BuIc]w~'VvHKmpJ+}s8y& XtP43.b[OA!*\Q<M%$ZgG52YloaRCn"`rj"""
    #myKey = getRandomKey()
    myMode = 'encrypt'  # set to 'encrypt' or 'decrypt'
    checkValidKey(myKey)
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')

def checkValidKey(key):
    keyLists = list(key)
    keyLetters = list(LETTERS)
    if keyLists.sort() != keyLetters.sort():
        sys.exit('There is an error in the key or symbol set.')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            # if symbol.isupper():
            #     translated += charsB[symIndex].upper()
            # else:
            #     translated += charsB[symIndex].lower()
            translated += charsB[symIndex]
        else:
            translated += symbol
    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)

    return ''.join(key)

if __name__ == '__main__':
    main()
