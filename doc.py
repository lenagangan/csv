import pandas as pd 
import glob

file_list = glob.glob('*.csv')
results = pd.DataFrame([])

for f in (file_list):
    df_each = pd.read_csv(f, low_memory=False)
    df_each['date'] = pd.to_datetime(f[4:11])
    results = results.append([df_each], ignore_index=True)

results.sort_values(by=['date'], inplace=True, ascending=True)
results['date'] = results['date'].dt.strftime('%m.%Y')
#results.to_csv("all"+".csv")
print (results.head())