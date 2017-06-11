import csv
# read csv file
with open('example.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    for row in readCSV:
        print(row)

# -----------------
with open('example.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        dates.append(row[0])
        colors.append(row[3])

    print(dates)
    print(colors)

    whatColor = input('What color do you wish to know the date of')
    coldex = colors.index(whatColor.lower())

    theDate = dates[coldex]
    print('The date of',whatColor,'is',theDate)