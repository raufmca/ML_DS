import numpy as np
import pandas as pd

df = pd.read_csv("D:\\ML_DS\\UNZIP_FOR_NOTEBOOKS_FINAL\\03-Pandas\\tips.csv")

df.head()

# conditional filtering
# to check bills more than 40

df['total_bill'] > 40

# catch anser in the bool_series

bool_series = df['total_bill'] > 40

# and pass this to data frame

df[bool_series]

# and it give the desired output

df[df['total_bill'] > 40]]

# can apply different filters

df[df['size'] > 4]

df[df['sex'] == 'Male']


# Multiple Conditional
# AND &
# OR |

df[(df['day'] =='Sun') | (df['day'] == 'Mon')]

