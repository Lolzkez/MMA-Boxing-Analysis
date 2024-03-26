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

agemmadf = pd.read_excel(survey, sheet_name=names[3], header=0)

agebxdf = pd.read_excel(survey, sheet_name=names[4], header=0)
agebxdf = agebxdf.fillna(0)

pp.suptitle("\nAge and...", fontsize=30)

pp.subplot(2,5,1)
pp.title("18-29 and MMA")
pp.pie(agemmadf["18-29"], labels=agemmadf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,5,2)
pp.title("30-39 and MMA")
pp.pie(agemmadf["30-39"][0:3], labels=agemmadf["Is Fan?"][0:3], autopct='%1.1f%%')

pp.subplot(2,5,3)
pp.title("40-49 and MMA")
pp.pie(agemmadf["40-49"], labels=agemmadf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,5,4)
pp.title("50-64 and MMA")
pp.pie(agemmadf["50-64"], labels=agemmadf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,5,5)
pp.title("65+ and MMA")
pp.pie(agemmadf["65+"], labels=agemmadf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,5,6)
pp.title("18-29 and Boxing")
pp.pie(agebxdf["18-29"], labels=agemmadf["Is Fan?"], autopct='%1.1f%%')

pp.subplot(2,5,7)
pp.title("30-39 and Boxing")
pp.pie(agebxdf["30-39"][0:3], labels=agemmadf["Is Fan?"][0:3], autopct='%1.1f%%')

pp.subplot(2,5,8)
pp.title("40-49 and Boxing")
pp.pie(agebxdf["40-49"][0:3], labels=agemmadf["Is Fan?"][0:3], autopct='%1.1f%%')

pp.subplot(2,5,9)
pp.title("50-64 and Boxing")
pp.pie(agebxdf["50-64"][0:3], labels=agemmadf["Is Fan?"][0:3], autopct='%1.1f%%')

pp.subplot(2,5,10)
pp.title("65+ and Boxing")
pp.pie(agebxdf["65+"][0:3], labels=agemmadf["Is Fan?"][0:3], autopct='%1.1f%%')

pp.subplots_adjust(wspace=0.7)
pp.ylim(-1, 2)
pp.show()
