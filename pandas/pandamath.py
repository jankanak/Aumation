import pandas as pd
df1=pd.read_excel('Book3.xlsx')
df1['v4']=df1['v1']+df1['v2']+df1['v3']
writer=pd.ExcelWriter('new.xlsx')
df1.to_excel(writer,'new')
writer.save()