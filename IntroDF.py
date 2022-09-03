import numpy as np

import pandas as pd

arr = np.arange(0,10)

print(arr)

arr1 = np.arange(1,26).reshape(5,5)

print(arr1)

print(arr1[2:,3:])

arr2 = pd.Series(arr)

print(arr2)


### Creating Data Frames

np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))
print(mydata)

# creating index
myindex = ['CA','NY','AZ','TX']

# creating columns
mycols = ['Jan','Feb','Mar']

df = pd.DataFrame(mydata)

print(mydata)

df = pd.DataFrame(mydata,myindex,mycols)

print(df)

print(df.info(),'\n')

print(df.index)