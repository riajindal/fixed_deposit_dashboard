import subprocess
import pandas as pd
from utility import master
from data_analysis.bucket_slabs import bucket
import os

print(os.getcwd())

subprocess.run(['python', r'C:\Users\riaji\PycharmProjects\deposit_project\data_extraction\index.py'])

df_kotak = pd.read_csv(r'C:\Users\riaji\PycharmProjects\deposit_project\kotak_slabs.csv')
df_kotak.drop(columns=df_kotak.columns.difference(['Tenure', 'General Rate']), inplace=True)
df_kotak.loc[:, 'Bank Name'] = 'Kotak'

for bank in master:
    bank.bucket_df = bucket(bank.name, bank.df)

bucket_master = df_kotak
for bank in master:
    bucket_master = pd.concat([bucket_master, bank.bucket_df], axis=0, ignore_index=True)

bucket_master.to_csv('bucket_master.csv', mode='w', index=False)

subprocess.run(['python', r'C:\Users\riaji\PycharmProjects\deposit_project\data_analysis\banks_historical_data.py'])
subprocess.run(['python', r'C:\Users\riaji\PycharmProjects\deposit_project\bank_historical_data\extract_historical.py'])

