import matplotlib.pyplot as pp
import matplotlib.ticker as tk
import pandas as pd
import numpy as np

ufc_file = "Excel Sheets/UFC PPV and Revenue.xlsx"
boxing_rev = "Excel Sheets/Boxing Revenue (ovr 1m PPV).xlsx"
boxing_ppv = "Excel Sheets/Boxing PPV.xlsx"
ufc_boxing_interest = "Excel Sheets/UFC vs Boxing Relative Search Interest Numbers.csv"
survey = "Excel Sheets/UFC and Boxing Survey Results.xlsx"

names = ["UFC and Boxing Survey Results", "Gender MMA", "Gender Boxing", "Age MMA", "Age Boxing", "Income MMA", "Income Boxing"]
sportsfan = pd.read_excel(survey, sheet_name=names[0], header=0)
sportsfan.columns = [col if 'Unnamed' not in str(col) else '' for col in sportsfan.columns]
sportsfan = sportsfan.fillna(0)

pp.subplot(1,2,1)
pp.title("Are Americans a fan of MMA?")
pp.pie(sportsfan.iloc[1][1:], labels = sportsfan.iloc[0][1:], autopct='%1.1f%%')

pp.subplot(1,2,2)
pp.title("Are Americans a fan of Boxing?")
pp.pie(sportsfan.iloc[2][1:4], labels = sportsfan.iloc[0][1:4], autopct='%1.1f%%')

pp.show()
