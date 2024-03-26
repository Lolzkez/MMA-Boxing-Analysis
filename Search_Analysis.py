import matplotlib.pyplot as pp
import matplotlib.ticker as tk
import pandas as pd
import numpy as np

ufc_file = "Excel Sheets/UFC PPV and Revenue.xlsx"
boxing_rev = "Excel Sheets/Boxing Revenue (ovr 1m PPV).xlsx"
boxing_ppv = "Excel Sheets/Boxing PPV.xlsx"
ufc_boxing_interest = "Excel Sheets/UFC vs Boxing Relative Search Interest Numbers.csv"
survey = "Excel Sheets/UFC and Boxing Survey Results.xlsx"

search = pd.read_csv(ufc_boxing_interest)
search["Month"] = pd.to_datetime(search["Month"])

pp.plot(search['Month'], search['Boxing: (Worldwide)'])
pp.plot(search['Month'], search['Ultimate Fighting Championship: (Worldwide)'])
pp.xlabel("Time (Years)")
pp.ylabel("Relative Search Interest (Percentage)")
pp.suptitle("Relative Search Interest of \nBoxing vs Ultimate Fighting Championship Over Time")
pp.legend(["Boxing", "UFC"])
pp.show()
