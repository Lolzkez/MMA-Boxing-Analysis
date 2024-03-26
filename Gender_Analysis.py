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

gendermmadf = pd.read_excel(survey, sheet_name=names[1])
gendermmadf = gendermmadf.fillna(0)

genderbxdf = pd.read_excel(survey, sheet_name=names[2])
genderbxdf = genderbxdf.fillna(0)
genderbxdf = genderbxdf.drop(3)

pp.suptitle("Gender and...", fontsize=30)
pp.subplot(2,2,1)
pp.title("Males and MMA")
pp.pie(gendermmadf["Male"], labels = gendermmadf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,2,2)
pp.title("Females and MMA")
pp.pie(gendermmadf["Female"], labels = gendermmadf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,2,3)
pp.title("Males and Boxing")
pp.pie(genderbxdf["Male"], labels = genderbxdf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,2,4)
pp.title("Females and Boxing")
pp.pie(genderbxdf["Female"], labels = genderbxdf["Is Fan?"][0:4], autopct='%1.1f%%')

pp.show()
