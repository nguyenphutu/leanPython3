from transpositionCipherEncryption import encryptMessage, decryptMessage
import detectEnglish
def main():

    myMessage = 'Btfcit ciefrnerpslk t ui eoe eBaeheroy6oiee,todea r yaltore cnpgmh cp terpslk.h ecllkot yh cp  a gs t d u r ' \
           'artt oareoeshthq  ygvyoieeuiy nt rco.eu e en  sb y  u  sf cpny  i hkgrr adrtwhvyoiee etyodo rhk adrttpiElhL’a btfcfteohpgmu r  ' \
           'eenuoti e sb ynlofdhcrtn cstra l2pslksiwlbeyoartastwtaai oatneysi e sb yTnh u of eetteysolnni.esdareoeeu  err.'

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)

def hackTransposition(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))
        decryptedText = decryptMessage(key=key, message=message)

        if detectEnglish.isEnglish(decryptedText):
            print('\nPossible encryption hack:')
            print('Key %s: %s \n' % (key, decryptedText[:100]))
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == "__main__":
    main()

