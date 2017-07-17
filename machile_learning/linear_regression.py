# Linear Regression
# Regression is a statistical method for modeling the relationship between a set of (independent) variables. Linear regression basically assumes a linear model. What is linear model? A model that is linear in parameters but can still use the independent variables in non-linear forms like x^2 and logx
#
# The model is defined by Hypothesis, which is a function of variables and parameters. H=a+bx
# In the equation above, [a,b] is the set of parameters and x is the independent variable. Our objective in regression, is to find the parameters [a,b]. Usually we are given a table of values of variables(x) and outputs(y) and asked to build a model that approximates the relationship between x and y.

import numpy as np
import csv

def hyp(x,theta,m):
    return np.dot(theta,x.reshape([2,m]))


# read data (x,y) from file
def readDataset(filename='ex1data1.txt'):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        datlist = list(reader)
    # return as numpy array
    return np.array(datlist, dtype='float32')


x, y = readDataset().T

def cost(x,y,theta):
    m = y.shape[0]
    h = np.dot(theta,x.reshape([2,m]))
    #print(h.shape,x.shape,y.shape,theta.shape)
    return np.sum(np.square(y-h))/(2.0*m)

def gd(x,y,theta,alpha = 0.005,iter=10000):
    m = y.shape[0]

    for i in range(iter):
        h = hyp(x,theta,m)
        error = h-y
        update = np.dot(x,error)
        theta = theta - ( (alpha*update)/m )

    print('theta',theta)
    print('cost',cost(x,y,theta))