import random, sys
from transpositionCipherEncryption import encryptMessage, decryptMessage

def main():
    random.seed(42)

    for i in range(20):  # run 20 tests
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # convert list to string
        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message.
        for key in range(1, len(message)):
            encrypted = encryptMessage(key = key, message = message)
            decrypted = decryptMessage(key = key, message = encrypted)

            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print(decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

if __name__ == "__main__":
    main()