import pandas as pd

df = pd.read_csv('student.csv', index_col='id', header=0, names=['id','name','class','mark','gender'])
print(df)


