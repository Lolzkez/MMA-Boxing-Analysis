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

incomemmadf = pd.read_excel(survey, sheet_name=names[5])
incomemmadf = incomemmadf.fillna(0)

incomebxdf = pd.read_excel(survey, sheet_name=names[6])

pp.suptitle("Income Bracket and...", fontsize=30)

pp.subplot(2,3,1)
pp.pie(incomemmadf["<50K"], labels = incomemmadf["Is Fan?"], autopct='%1.1f%%')
pp.title("<50k Per Year and MMA")

pp.subplot(2,3,2)
pp.pie(incomemmadf["50-100K"][:3], labels = incomemmadf["Is Fan?"][:3], autopct='%1.1f%%')
pp.title("50K to 100K Per Year and MMA")

pp.subplot(2,3,3)
pp.pie(incomemmadf["100K+"], labels = incomemmadf["Is Fan?"], autopct='%1.1f%%')
pp.title("100K+ Per Year and MMA")

pp.subplot(2,3,4)
pp.pie(incomemmadf["<50K"], labels = incomemmadf["Is Fan?"], autopct='%1.1f%%')
pp.title("<50k Per Year and Boxing")

pp.subplot(2,3,5)
pp.pie(incomemmadf["50-100K"][:3], labels = incomemmadf["Is Fan?"][:3], autopct='%1.1f%%')
pp.title("50K to 100K Per Year and Boxing")

pp.subplot(2,3,6)
pp.pie(incomemmadf["100K+"][:3], labels = incomemmadf["Is Fan?"][:3], autopct='%1.1f%%')
pp.title("100K+ Per Year and Boxing")

pp.show()
