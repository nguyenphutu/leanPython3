# local var
x = 10

def example():
    # global var
    globalx = x
    globalx += 5

    return globalx

x = example()
print(x)