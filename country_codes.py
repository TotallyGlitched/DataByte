import pandas as pd

file_c=pd.read_csv('country.csv')
print(file_c)
dictionary=file_c.to_dict()
print(dictionary)