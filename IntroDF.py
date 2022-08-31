import numpy as np

import pandas as pd

arr = np.arange(0,10)

print(arr)

arr1 = np.arange(1,26).reshape(5,5)

print(arr1)

print(arr1[2:,3:])

arr2 = pd.Series(arr)

print(arr2)