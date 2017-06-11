text = 'Sample Text to Save\nNew Line'

saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()

# Appending File

appendMe = '\nNew line to append'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()

# read from a file

readMe = open('exampleFile.txt','r').readlines()
# ['Sample Text to Save\n', 'New Line\n', 'New line to append']
print(readMe)
readMe = open('exampleFile.txt','r').read()
# Sample Text to Save
# New Line
# New line to append
print(readMe)