# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(np_baseball)
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)

# In ra phan tu hang 2 cot 1
# giong trong ma tran hang i cot j A[i,j]
print(np_baseball[1,0])
# in ra phan tu hang 1 2 cot 2 -> [102.7 98.5]
print(np_baseball[1:3,1])