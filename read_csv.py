import pandas as pd
import numpy as np

df = pd.read_csv('ecommerce_data.csv', encoding='unicode_escape')
print(df.head())

print("test done")
print("Development Part 1")

# this is to sum the numbers
def sum(a,b):
    return a+b
print(sum(1,2))