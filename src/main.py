import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


out_dir = "./out"                                       ##  output path
url = r"https://smart-lab.ru/q/shares_fundamental/"     ##  raw url

max_PE = 16
max_PS = 4
max_PB = 1
max_ND_EBITDA = 2.5
#max_EV_EBITDA = 10


print("Downloading...")
tables = pd.read_html(url)  ##  Returns list of tables on page
market_data = tables[0]
companies = set(market_data["Название"])
pe = list(market_data["P/E"])
#yields.sorted

##  Choose dataframe with price ratios
print("Creating table...")
low_P_ratio = market_data
print("Forming data...")
low_P_ratio = low_P_ratio[(low_P_ratio["P/E"] < max_PE) & (low_P_ratio["P/E"] > 0)] ##  Price/earnings ratio
low_P_ratio = low_P_ratio[(low_P_ratio["P/S"] < max_PS) & (low_P_ratio["P/S"] > 0)] ##  Price/sales ratio
low_P_ratio = low_P_ratio[(low_P_ratio["P/B"] < 4) & (low_P_ratio["P/B"] > 0)]      ##  Price/book value ratio
low_P_ratio = low_P_ratio[(low_P_ratio["ДД ао, %"] is not None) & (low_P_ratio["ДД ао, %"] != "0.0%")]                              ##  With dividends
low_P_ratio = low_P_ratio[low_P_ratio["долг/EBITDA"] < max_ND_EBITDA]               ##  With low debd load

print("Sorting data...")
lowest_P_ratio = low_P_ratio.sort_values(by = ["P/E", "P/S", "P/B", "долг/EBITDA", "EV/EBITDA"], ascending = True, ignore_index = False)

"""
companies_PE = market_data[["Название", "P/E"]]
##  Select companies with (0 < P/E < max_PE)
low_PE = market_data.loc[(market_data["P/E"] < max_PE) & (market_data["P/E"] > 0), ["Название", "P/E"]]
low_PS = market_data.loc[(market_data["P/S"] < max_PS) & (market_data["P/S"] > 0), ["Название", "P/S"]]
low_PB = market_data.loc[(market_data["P/B"] < max_PB) & (market_data["P/B"] > 0), ["Название", "P/B"]]
low_ND_EBITDA = market_data.loc[market_data["долг/EBITDA"] < max_ND_EBITDA, ["Название", "долг/EBITDA"]]

low_PE.info()
low_PS.info()
low_PB.info()
low_ND_EBITDA.info()
#high_DY = market_data.loc[()]

#lowest_PE = ???????????????
#lowest_PS = 
#lowest_PB = 
"""
if not os.path.exists(out_dir):
    Path(out_dir).mkdir(parents = True, exist_ok = True)
    print("Out directory was created")
with open("./out/out.csv", 'w') as f:
    f.write(lowest_P_ratio.to_csv())
    print("CSV file writen")

with open("./out/out.xlsx", 'w') as f:
    lowest_P_ratio.to_excel("./out/out.xlsx")
    print("Excel file writen")

print("Success")
