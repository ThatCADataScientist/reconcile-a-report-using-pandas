# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df['state']=df['state'].map(lambda x: x.lower())
df['total'] = df['Jan']+df['Feb']+df['Mar']
sum_row = df[['Jan','Feb','Mar','total']].sum()
df_final = df.append(sum_row,ignore_index=True)
df_final
# Code ends here


# --------------
import requests

# Code starts here
url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1=df1.iloc[11:,:]
df1=df1.rename(columns=df1.iloc[0,:]).iloc[1:,:]
df1['United States of America'] = df1['United States of America'].str.strip()
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)
mapping=df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6, 'abbr',value='Nan')
df_final['abbr']=df_final['state'].map(mapping)


# --------------
# Code stars here
#add the df name to both below

df_final.loc[(df_final.state=='mississipi'),'abbr']='MS'
df_final.loc[(df_final.state=='tenessee'),'abbr']='TN'
# Code ends here


# --------------
# Code starts here
df_sub=df_final[['abbr','Jan','Feb','Mar','total']].groupby('abbr').sum()
print(df_sub.shape)
formatted_df=df_sub.applymap(lambda x: '$'+str(x))
print(formatted_df.shape)
# Code ends here


# --------------
# Code starts here

sum_row=pd.DataFrame(df_final[['Jan','Feb','Mar','total']].sum())
df_sub_sum= sum_row.transpose()
df_sub_sum=df_sub_sum.applymap(lambda x: '$'+str(x))
final_table = df_sub_sum.append(formatted_df)
final_table.rename(columns={'0': 'Total'}, inplace=True)

# Code ends here


# --------------
# Code starts here
# df_sub['total']=df[['Jan','Feb','Mar']].sum(axis=1)
# df_sub
df_sub['total'].plot(kind='pie')
plt.show()

# Code ends here


