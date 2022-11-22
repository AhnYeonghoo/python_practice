import pandas as pd

tup_data = ["영민", "2010-05-01", "여", True]
ar = pd.Series(tup_data, index=['이름', '생년월일','성별', '학생여부'])
print(ar)
print(ar[0])
print(ar['이름'])

print('\n')
print(ar[[1, 2]])
print(ar[['생년월일', '성별']])
print(ar[1 : 2])
print(
'\n'
)
print(ar['생년월일' : '성별'])