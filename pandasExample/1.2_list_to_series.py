list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
lr = pd.Series(list_data)
print(lr)

idx = lr.index
val = lr.values
print(idx)
print('\n')
print(val)