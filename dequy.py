# tinh giai thua
def dequy(num):
    if num == 0:
        return 1
    return num*dequy(num-1)

print(dequy(3))