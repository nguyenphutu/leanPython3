import os
# print where working directory
curDir = os.getcwd()
print(curDir)

# create new directory
os.mkdir('newDir')

import time

time.sleep(2)
# rename
os.rename('newDir','newDir2')
time.sleep(2)
# remove
os.rmdir('newDir2')

# search in cmd >> python >>>help(os) to know more