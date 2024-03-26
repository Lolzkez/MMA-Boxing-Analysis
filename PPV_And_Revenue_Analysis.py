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

gendermmadf = pd.read_excel(survey, sheet_name=names[1], header=0)
gendermmadf.columns = [col if 'Unnamed' not in str(col) else '' for col in gendermmadf.columns]

genderbxdf = pd.read_excel(survey, sheet_name=names[2], header=0)
genderbxdf.columns = [col if 'Unnamed' not in str(col) else '' for col in genderbxdf.columns]

agemmadf = pd.read_excel(survey, sheet_name=names[3], header=0)
agemmadf.columns = [col if 'Unnamed' not in str(col) else '' for col in agemmadf.columns]

agebxdf = pd.read_excel(survey, sheet_name=names[4], header=0)
agebxdf.columns = [col if 'Unnamed' not in str(col) else '' for col in agebxdf.columns]

incomemmadf = pd.read_excel(survey, sheet_name=names[5], header=0)
incomemmadf.columns = [col if 'Unnamed' not in str(col) else '' for col in incomemmadf.columns]

incomebxdf = pd.read_excel(survey, sheet_name=names[6], header=0)
incomebxdf.columns = [col if 'Unnamed' not in str(col) else '' for col in incomebxdf.columns]

ufc_ppv_rev = pd.read_excel(ufc_file, header=0)
ufc_ppv_rev.columns = [col if 'Unnamed' not in str(col) else '' for col in ufc_ppv_rev.columns]
ufc_ppv_rev["Date"] = pd.to_datetime(ufc_ppv_rev["Date"])
ufc_ppv_rev['Revenue(est)'] = ufc_ppv_rev['Revenue(est)'].fillna(ufc_ppv_rev["Revenue(est)"].mean())
ufc_ppv_rev = ufc_ppv_rev.sort_values(by=["Date"])

boxing_rev_df = pd.read_excel(boxing_rev, header=0)
boxing_rev_df.columns = [col if 'Unnamed' not in str(col) else '' for col in boxing_rev_df.columns]
boxing_rev_df["Date"] = pd.to_datetime(boxing_rev_df["Date"])
boxing_rev_df['Revenue'] = boxing_rev_df['Revenue'].fillna(boxing_rev_df["Revenue"].mean())
boxing_rev_df = boxing_rev_df.sort_values(by=["Date"])

boxing_ppv_df = pd.read_excel(boxing_ppv, header=0)
boxing_ppv_df["Date"] = pd.to_datetime(boxing_ppv_df["Date"])

pp.subplot(2,2,1)
pp.plot(ufc_ppv_rev['Date'], ufc_ppv_rev['Buy Rate'], color='blue')
months_since_start = ((ufc_ppv_rev['Date'].dt.year - ufc_ppv_rev['Date'].dt.year.min()) * 12 +
                      (ufc_ppv_rev['Date'].dt.month - ufc_ppv_rev['Date'].dt.month.min())).values
coeff_dbr = np.polyfit(months_since_start, ufc_ppv_rev['Buy Rate'], 1)
tval_dbr = np.poly1d(coeff_dbr)
pp.xlabel("Time (Years)")
pp.ylabel("PPV Buy Rate")
pp.title("UFC PPV Buy Rate Over Time")
def format_large_tick_val(x, pos):
    if x >= 1e6:
        return '{:,.2f}M'.format((x / 1e6))
    else:
        return '{:g}K'.format(x / 1e3)
pp.gca().yaxis.set_major_formatter(tk.FuncFormatter(format_large_tick_val))
pp.plot(ufc_ppv_rev['Date'], tval_dbr(months_since_start), color='green')
slope = coeff_dbr[0]
pp.text(ufc_ppv_rev['Date'][1], ufc_ppv_rev['Buy Rate'].min(), f'Slope: {slope:.2f}', va='top', ha='right', color='green')

pp.subplot(2,2,2)
pp.plot(ufc_ppv_rev['Date'], ufc_ppv_rev['Revenue(est)'])
months_since_start = ((ufc_ppv_rev['Date'].dt.year - ufc_ppv_rev['Date'].dt.year.min()) * 12 +
                      (ufc_ppv_rev['Date'].dt.month - ufc_ppv_rev['Date'].dt.month.min())).values
coeff_dbr = np.polyfit(months_since_start, ufc_ppv_rev['Revenue(est)'], 1)
tval_dbr = np.poly1d(coeff_dbr)
pp.xlabel("Time (Years)")
pp.ylabel("Revenue (in US$)")
pp.title("Estimated Revenue of UFC Events Over Time")
def format_large_tick_val(x, pos):
    if x >= 1e6:
        return '{:,.2f}M'.format((x / 1e6))
    else:
        return '{:g}K'.format(x / 1e3)
pp.gca().yaxis.set_major_formatter(tk.FuncFormatter(format_large_tick_val))
pp.plot(ufc_ppv_rev['Date'], tval_dbr(months_since_start), color='green')
slope = coeff_dbr[0]/1e3
pp.text(ufc_ppv_rev['Date'][0], ufc_ppv_rev['Revenue(est)'].min(), f'Slope: {slope:.2f}K', va='top', ha='left', color='green')

pp.subplot(2,2,3)
pp.plot(boxing_ppv_df['Date'], boxing_ppv_df['Buy Rate'], color='blue')
months_since_start = ((boxing_ppv_df['Date'].dt.year - boxing_ppv_df['Date'].dt.year.min()) * 12 +
                      (boxing_ppv_df['Date'].dt.month - boxing_ppv_df['Date'].dt.month.min())).values
coeff_dbr = np.polyfit(months_since_start, boxing_ppv_df['Buy Rate'], 1)
tval_dbr = np.poly1d(coeff_dbr)
pp.xlabel("Time (Years)")
pp.ylabel("PPV Buy Rate")
pp.title("Boxing PPV Buy Rate Over Time")
def format_large_tick_val(x, pos):
    if x >= 1e6:
        return '{:,.2f}M'.format((x / 1e6))
    else:
        return '{:g}K'.format(x / 1e3)
pp.gca().yaxis.set_major_formatter(tk.FuncFormatter(format_large_tick_val))
pp.plot(boxing_ppv_df['Date'], tval_dbr(months_since_start), color='green')
slope = coeff_dbr[0]
pp.text(boxing_ppv_df['Date'][0], boxing_ppv_df['Buy Rate'].min(), f'Slope: {slope:.2f}', va='top', ha='left', color='green')

pp.subplot(2,2,4)
months_since_start = ((boxing_rev_df['Date'].dt.year - boxing_rev_df['Date'].dt.year.min()) * 12 +
                      (boxing_rev_df['Date'].dt.month - boxing_rev_df['Date'].dt.month.min())).values
coeff_dbr = np.polyfit(months_since_start, boxing_rev_df['Revenue'], 1)
tval_dbr = np.poly1d(coeff_dbr)
pp.plot(boxing_rev_df['Date'], boxing_rev_df['Revenue'])
pp.xlabel("Time (Years)")
pp.ylabel("Revenue (in US$)")
pp.title("Revenue of Boxing Events with Over 1M PPV Buys Over Time")
def format_large_tick_val(x, pos):
    if x >= 1e6:
        return '{:,.2f}M'.format((x / 1e6))
    else:
        return '{:g}K'.format(x / 1e3)
pp.gca().yaxis.set_major_formatter(tk.FuncFormatter(format_large_tick_val))
pp.plot(boxing_rev_df['Date'], tval_dbr(months_since_start), color='green')
slope = coeff_dbr[0]/1e3
pp.text(5, 30000000, f'Slope: {slope:.2f}K', va='top', ha='left', color='green')


pp.show()