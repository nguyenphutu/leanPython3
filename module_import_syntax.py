import statistics as st

exampleList = [4,5,6,1,2,5,7,8,9,10.23]
# mean, variance, median, stdev ... function of statistics
x = st.mean(exampleList)
print(x)

# or
from statistics import mean

y = mean(exampleList)
print(y)
