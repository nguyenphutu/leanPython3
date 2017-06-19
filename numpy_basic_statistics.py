import numpy as np
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
np_baseball = np.array(baseball)
# Create numpy array np_height that is equal to first column of np_baseball.
# Create np_height from np_baseball
np_height = np_baseball[:,0]
print(np_height)
# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))