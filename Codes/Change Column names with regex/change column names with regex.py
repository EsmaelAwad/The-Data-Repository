import pandas as pd
import re

#The first method forces you to think in python!

d = {'col1':['06-31-2022','06-30-2022','06-29-2022'],\
     'col2':[200450,250000,153005],\
         'col3':['ahmed','mohamed','salem'],\
            'col4':[500,600,430] }
    
df= pd.DataFrame(data=d)
print(df)

for col in df.columns:

    df[col] = df[col].astype('str')


df_list = df.values.tolist()
print(df_list)

#If It Matched, Get me the match!

dated = '03-06-2022'

match = re.match(r'\d{2}-\d{2}-\d{4}',dated)
print(match)

if match:
    print(match[0])



my_df = pd.DataFrame()

date_list = []
salesman_list = []
sales_list = []
quantity_list = []

for lis in df_list:
    for item in lis:
        date_match = re.match(r'\d{2}-\d{2}-\d{4}',item)
        quantity_match = re.match(r'\d{3}(?!\d+)',item)
        sales_match = re.match(r'\d{4,6}',item)
        salesman_match = re.match(r'[a-zA-Z]+',item)
        
        if date_match:
            datedd = date_match[0]
            date_list.append(datedd)
        if quantity_match:
            matchq = quantity_match[0]
            quantity_list.append(matchq)
        if salesman_match:
            matchman = salesman_match[0]
            salesman_list.append(matchman)
        if sales_match:
            sales = sales_match[0]
            sales_list.append(sales)

#Now we have a list of dates,Salesmen,Sales Amounts, Quantites, no matter how many rows are added later, the algorithm will take care of it!

my_df['Date'] = date_list
my_df['Salesman'] = salesman_list
my_df['Sales Amount'] = sales_list
my_df['Quantity'] = quantity_list
print(my_df)
