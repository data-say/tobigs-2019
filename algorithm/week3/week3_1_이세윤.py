import pandas as pd
import numpy as np

df = pd.read_csv(input())
df['IQ'] = df['IQ'].str.extract('(\d+)')
R = int(df.IQ.isnull().sum() * 100 / len(df))
df.loc[df['IQ'].notnull(), 'IQ'] = df.loc[df['IQ'].notnull(), 'IQ'].astype(int)
df['IQ'] = df['IQ'].groupby(df['Gender']).apply(lambda x: x.fillna(int(x.mean())))
df['expectIQ'] = 0
df.loc[df['Gender'] == 'M', 'expectIQ'] = df['Height'] - 70
df.loc[df['Gender'] == 'F', 'expectIQ'] = df['Height'] - 60
E = int(sum(abs(df['expectIQ'] - df['IQ'])) / len(df))
H = int((((df['Gender'] == 'F') & df['Height'].between(158, 162, inclusive=True)) | ((df['Gender'] == 'M') & df['Height'].between(168, 172, inclusive=True))).sum() * 100 / len(df))
print(R, E, H)
print('GodHyeIn' if R > 25 or E > 5 or H > 50 else 'GodDaeWoong')