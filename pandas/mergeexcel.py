# import pandas as pd

# with open('C:/Users/SunMoon Computer/Desktop/New folder/Book1.xlsx','r')as file:
#     print(file)
    
import pandas as pd
excel1='C:/Users/SunMoon Computer/Desktop/New folder/Book1.xlsx'
df1=pd.read_excel(excel1)
print(df1)
excel2='C:/Users/SunMoon Computer/Desktop/New folder/Book2.xlsx'
df2=pd.read_excel(excel2)
print(df2)

v1=df1[['name']]
v2=df2[['dept']]
dataframes=[v1,v2]
join=pd.concat(dataframes,sort=False,ignore_index=True)
join.to_excel('output4.xlsx')