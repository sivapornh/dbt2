import pandas as pd

df = pd.read_csv('ecommerce_data.csv', encoding='unicode_escape')
df = df.iloc[0:5]