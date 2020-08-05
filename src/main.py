import pandas as pd
import matplotlib.pyplot as plt


url = r"https://smart-lab.ru/q/shares_fundamental/"

max_PE = 16
max_PS = 4
max_PB = 1
max_ND_EBITDA = 2.5
#max_EV_EBITDA = 10


tables = pd.read_html(url)  ##  Returns list of tables on page
market_data = tables[0]
companies = set(market_data["Название"])
pe = list(market_data["P/E"])
#yields.sorted

##  Choose dataframe with P/E, yields
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
