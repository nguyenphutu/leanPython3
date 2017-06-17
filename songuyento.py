# ktra so nguyen to
import math
def ktra(n):
    can_bac_2 = math.sqrt(n)
    for i in range(2,math.ceil(can_bac_2)+1):
        if n%i == 0:
            return False
    return True

for snt in range(1,101):
    if ktra(snt):
        print(snt, "la so nguyen to")


