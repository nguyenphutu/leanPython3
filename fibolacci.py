def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber:
            return
        if cur >= startNumber:
            yield cur
for i in SubFib(0, 20):
    print(i)

for i in F():
    print(i)

# ---------------

# def fib(num):
#     if num <= 1:
#         return num
#     return fib(num-2) + fib(num-1)
#
# for i in range(10):
#     print(i,fib(i))