import numpy as np
import pandas as pd

df = pd.read_csv("D:\\ML_DS\\UNZIP_FOR_NOTEBOOKS_FINAL\\03-Pandas\\tips.csv")

print(df)

# printing columns

print(df.columns)

# to print first 5 lines

df.head()

# to check how many rows

df.index

# to get the df information

df.info()

#Descriptive statistics include those that summarize the central
#tendency, dispersion and shape of a

df.describe()

# to get specific file

df['total_bill']

# to get multiple bills

df[['total_bill','tip']]

# to add new column

df['tip %'] = 100 * df['tip'] / df['total_bill']

# to round of tip% 2 decimals

df['tip %'] = np.round(df['tip %'],2)

# to know the shape

df.shape

# to set index from columns

df.set_index('Payment ID') # this action is temp

# to set permanently

df = df.set_index('Payment ID')

# to revert back the set index

df.reset_index()

# same way to make it permanent

df = df.reset_index()

# to get the integer location indexes

df.iloc[2]

# to get the slice using

df.iloc[2:5]

# to get through string index

df.loc['Sun4608']