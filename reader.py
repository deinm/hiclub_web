import pandas as pd

data = pd.read_excel('2019-2.xls', encoding='utf-8')

# print(data.head())

print(data['Course Number'])