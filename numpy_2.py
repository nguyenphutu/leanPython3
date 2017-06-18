# height is available as a regular list
height = [74, 74, 72, 72, 73, 69, 69, 71, 76, 73]
# Import numpy
import numpy as np

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
np_height_m = np_height*0.0254

# Print np_height_m
print(np_height_m)

# Create the light array have np_height_m < 1.9
light = np_height_m<1.9

# Print out light
print(light)

# Print out np_height_m of all height whose np_height_m is below 1.9
print(np_height_m[np_height_m<1.9])

