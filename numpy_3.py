import numpy as np

print(np.array([True, 1, 2]))
print(np.array([3, 4, False]))

# array in np chi chua duy nhat 1 kieu du lieu
# Arue se bi convert ve 1
# False se bi convert ve 0
print(np.array([True, 1, 2]) + np.array([3, 4, False]))

# Select element in array same in list
a = np.array([2, 4, 5, 2, 1, 9])
print(a[3])
print(a[:4])
