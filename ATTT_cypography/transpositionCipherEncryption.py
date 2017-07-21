import math

# Transposition Cipher Encryption
def encryptMessage(message, key):
    cipertext = ['']*key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipertext[col] += message[pointer]
            pointer = pointer + key

    return ''.join(cipertext)

def decryptMessage(message, key):
    numOfColumns = math.ceil(len(message)/key)
    numOfRows = key
    numOfShadedBox = (numOfColumns*numOfRows) - len(message)

    plaintext = ['']*numOfColumns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if ((col == numOfColumns) or (col == numOfColumns - 1 and (row >= (numOfRows - numOfShadedBox)))):
            col = 0
            row += 1
    return ''.join(plaintext)


def main():
    mess = 'Brute force is the technique of trying every possible key until you find the correct one. Because there are only 26 possible keys, it would be easy for a cryptanalyst to write a hacking program than decrypts with every possible key. Then they could look for the key that decrypts to plain English. Let’s add a brute force feature to the program.'
    key = 3
    ciphertext = encryptMessage(message=mess, key=key)
    print(ciphertext)
    plaintext = decryptMessage(ciphertext, key=key)
    print(plaintext)

if __name__ == '__main__':
    main()