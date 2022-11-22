import pandas as pd

exam_data = { '이름' : [ '서준', '우현', '인아'],
              '수학' : [ 90, 80, 70 ],
              '영어' : [ 98, 89, 95 ],
              '음악' : [ 85, 95, 100 ],
              '체육' : [ 100, 90, 90 ]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

english = df.영어
print(english)
print(type(english))

music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')
math2 = df[['수학']]
print(math2)
print(type(math2))