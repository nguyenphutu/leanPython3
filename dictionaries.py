# dic have Keys and value. Key will be a single element values can be anything
# list , function...

exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}
print(exDict)
print(exDict['Jack'])

exDict['Tim'] = 14
print(exDict)
exDict['Tim'] = 16
print(exDict)
# -> dict have to have unique keys otherwise it
# delete element of dict
del exDict['Tim']
print(exDict)

exDict2 = {'Jack':[15,'black'],'Bob':22,'Alice':12,'Kevin':17}
print(exDict2['Jack'][1])