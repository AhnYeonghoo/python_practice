import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age',' fare']]
print(df.tail())
print('\n')
print(type(df))

addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

subtraction = addition - df
print('\n')
print(type(subtraction))