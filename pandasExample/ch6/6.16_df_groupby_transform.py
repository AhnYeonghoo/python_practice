import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
print(std_all);print('\n')
print(type(std_all));print('\n')

std_fare = grouped.fare.std()
print(std_fare)
print('\n')
print(type(std_fare))

def min_max(x):
    return x.max() - x.min()
agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())

agg_sep = grouped.agg(['min', 'max'])
print(agg_sep.head())

age_mean = grouped.age.mean()
print(age_mean)
print('\n')

age_std = grouped.age.std()
print(age_std)
print('\n')

for key, group in grouped_age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin: ', key)
    print(group_zscore.head())
    print('\n')
    
def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]])
