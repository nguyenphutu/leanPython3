# how to use file __init__.py
# de dinh nghia thu muc laf 1 package cua python
# chung ta co tje import cac module trong thu muc do

import test.tesst

x = [str(i)*(i%3>0)*(i%5>0) + 'Fizz'*(i%3==0) + 'Buzz'*(i%5==0) for i in range(1,101)]
print(x)