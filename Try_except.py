import csv
with open('example.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        dates.append(row[0])
        colors.append(row[3])
    print(dates)
    print(colors)
    try:
        whatColor = input('What color do you wish to know the date of')
        coldex = colors.index(whatColor.lower())
        theDate = dates[coldex]
        print('The date of',whatColor,'is',theDate)
    # except Exception, NameError ...:
    except Exception as e:
        print(e)
