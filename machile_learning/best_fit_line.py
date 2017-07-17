import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
print(plt.style.available)


# read data (x,y) from file
def readDataset(filename='ex1data1.txt'):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        datlist = list(reader)
        print(datlist)
    # return as numpy array
    return np.array(datlist, dtype='float32')


xs, ys = readDataset().T

# y = mx + b

def bet_fit_line_m_b(x, y):
    m = (((np.mean(x) * np.mean(y)) - np.mean(x * y)) /
         ((np.mean(x) * np.mean(x)) - np.mean(x * x)))

    b = np.mean(y) - m * np.mean(x)

    return m, b


m, b = bet_fit_line_m_b(xs, ys)
regression_line = [(m * x + b) for x in xs]
predict_x = 16
predict_y = (m * predict_x) + b

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, edgecolors='red')
plt.plot(xs, regression_line)

plt.show()
