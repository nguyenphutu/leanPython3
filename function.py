# define the function
def example():
    print('basic function')

# call function
example()

# muti function
def add(num1,num2):
    return num1+num2
print(add(3,4))


def simple():
    pass
def simple(num1,num2 = 5):
    print(num1,num2)
simple(3)

def basic_window(width,height,font='abc',
                 bgc = 'w'
                 ):
    print(width,height,bgc,font)
basic_window(320,210,bgc='black')