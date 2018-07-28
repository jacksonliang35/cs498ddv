import pandas as pd
import numpy as np

''' Excel to CSV '''
'''
data = pd.read_excel("./table_01_69_1.xlsx")
# print(data.dtypes)
data = data.iloc[0:101]
data.to_csv("./cs498ddv_data.csv", index=False)
'''

''' CSV processing '''
data = pd.read_csv("./cs498ddv_data.csv")
ignore_list = ["UrbanArea", "PopulationGroup", "STPercent", "STRank", "LTPercent", "LTRank"]
nd = {"Year": [col for col in data.columns if col not in ignore_list],
      "Very large": [0] * 27,
      "Large": [0] * 27,
      "Medium": [0] * 27,
      "Small": [0] * 27}
for i in range(101):
    for y in range(2, 29):
        nd[data.iloc[i].PopulationGroup][y-2] += data.iloc[i][y]
# print(nd)
ndata = pd.DataFrame(data=nd, dtype=np.int32)
ndata.to_csv("./total_count.csv", index=False)
