
def caesarCipher(message, mode, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num_symbol = LETTERS.find(symbol)
            if mode in ['encrypt', 'e', 'E']:
                num_symbol = num_symbol + key
            elif mode in ['decrypt', 'd', 'D']:
                num_symbol = num_symbol - key

            if num_symbol >= len(LETTERS):
                num_symbol = num_symbol - len(LETTERS)
            elif num_symbol < 0:
                num_symbol = num_symbol + len(LETTERS)

            translated = translated + LETTERS[num_symbol]
        else:
            translated = translated + symbol

    return translated

mess = "This is my secret message."
key = 3
encript = caesarCipher(message=mess, key=key, mode='e')
decript = caesarCipher(message=encript, key=key, mode='d')
print(encript)
print(decript)

def caesarCipherHacker(message):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num_symbol = LETTERS.find(symbol)
                num_symbol = num_symbol - key
                if num_symbol < 0:
                    num_symbol = num_symbol + len(LETTERS)

                translated = translated + LETTERS[num_symbol]
            else:
                translated = translated + symbol
        print("key = {0}: {1}".format(key, translated))
    return
print("\nCrack caesar cipher\n")
caesarCipherHacker("WKLV LV PB VHFUHW PHVVDJH.")
