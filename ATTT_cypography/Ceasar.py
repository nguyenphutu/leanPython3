#Plaintext "Meet me after the toga party"

#Ciphertext "PHHW PH DIWHU WKH WRJD SDUWB"

#Việc mã hoá được thực hiện đơn giản là thay mỗi chữ trong bản rõ bằng chữ thứ k tiếp theo trong bảng chữ cái.

#   Về toán học, nếu ta gán  số thứ tự cho mỗi chữ trong bảng chữ cái. Các chữ  ở dòng trên có số thứ tự tương ứng là số ở dòng dưới:
# 	a b c d e f g h i j k  l  m
# 	0 1 2 3 4 5 6 7 8 9 10 11 12
# 	n  o  p  q  r  s  t  u  v  w  x  y  z
# 	13 14 15 16 17 18 19 20 21 22 23 24 25
# thì mã Ceasar được định nghĩa qua phép tịnh tiến các chữ như sau:
# 		c = E(p) = (p + k) mod (26)
# 		p = D(c) = (c – k) mod (26)

import numpy as np

def key_word():
    key_word = {}
    word = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    for w in word:
        key_word[i] = w
        i += 1
    return key_word


def Ciphertext_to_Plaintext(Ciphertext):
    key_w = key_word()
    C = Ciphertext.lower()
    number_c = []
    for w in C:
        if w == ' ':
            number_c.append(999)
        else:
            for k, v in key_w.items():
                if key_w[k] == w:
                    number_c.append(k)

    number_c = np.array(number_c)
    for i in range(26):
        p = []
        demo = np.absolute(number_c - i)
        for k in demo:
            if k in key_w.keys():
                p.append(key_w[k])
            else: p.append(' ')
        print(''.join(p))


Ciphertext_to_Plaintext("PHHW PH DIWHU WKH WRJD SDUWB")

