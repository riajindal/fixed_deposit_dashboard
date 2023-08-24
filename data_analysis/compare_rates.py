import pandas as pd
from utility import master

df = pd.DataFrame(index=list(range(3651)))
for bank in master:
    df[bank.name] = None
    for index, row in bank.df.iterrows():
        min = row['Min Value']
        max = row['Max Value']
        # print(index)
        for i in range(min, max + 1):
            # print(df[bank_list[0].name].loc[i])
            df.loc[i, bank.name] = bank.df.at[index, 'General Rate']

# df.to_csv('comparison.csv', mode='w')
