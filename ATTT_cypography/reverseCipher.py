# Reverse Cipher mã hóa một tin nhắn bằng cách in theo thứ tự ngược lại. Vì vậy "Hello world!" Mã hóa để "!dlrow olleH".
# Để giải mã, bạn chỉ cần đảo ngược thông điệp đã được đảo ngược để có được thông báo ban đầu.

# Reverse Cipher

def reverseCipher(message):
    translated = ''
    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    return translated

Cipher = reverseCipher("Hello world!")
decrypt = reverseCipher(Cipher)
print(Cipher)
print(decrypt)

