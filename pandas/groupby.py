import pandas as pd
df = pd.read_excel("./input/aaaa.xlsx", engine = "openpyxl")
a=df.groupby('품목').sum()
# a['total']=a['수량']*a['가격']
a.insert(2,'total',a['수량']*a['가격'])
print(a)
# a.to_excel("out.xlsx")
