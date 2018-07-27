import pandas as pd

data = pd.read_excel("./table_01_69_1.xlsx")
# print(data.dtypes)
data = data.iloc[0:101]
data.to_csv("./cs498ddv_data.csv", index=False)
