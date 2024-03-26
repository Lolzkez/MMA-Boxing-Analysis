import requests
import pandas as pd
from bs4 import BeautifulSoup
import openpyxl

table = pd.read_html('https://en.wikipedia.org/wiki/Pay-per-view#Worldwide')
boxing_rev = table[3]
boxing_df = table[5]
ufc_df = table[7]

def a(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

ufc_list = [ufc_df[col].tolist() for col in ufc_df.columns]
for i in range(len(ufc_list)):
    for j in range(len(ufc_list[i])):
        ufc_list[i][j] = a(str(ufc_list[i][j]))

boxing_list = [boxing_df[col].tolist() for col in boxing_df.columns]
for i in range(len(boxing_list)):
    for j in range(len(boxing_list[i])):
        boxing_list[i][j] = a(str(boxing_list[i][j]))

boxing_rev_list = [boxing_rev[col].tolist() for col in boxing_rev.columns]
for i in range(len(boxing_rev_list)):
    for j in range(len(boxing_rev_list[i])):
        boxing_rev_list[i][j] = a(str(boxing_rev_list[i][j]))

ufc_dict = {'Date': ufc_list[0], 'Event': ufc_list[1], 'Headline': ufc_list[2], 'Buy Rate': ufc_list[3], 'Revenue(est)': ufc_list[4]}
ufc_df = pd.DataFrame(ufc_dict)

boxing_dict = {'Date': boxing_list[0], 'Fight': boxing_list[1], 'Result': boxing_list[2], 'Carrier': boxing_list[3], 'Buy Rate': boxing_list[4]}
boxing_df = pd.DataFrame(boxing_dict)

boxing_rev_dict = {'Date': boxing_rev_list[0], 'Fight': boxing_rev_list[1], 'Networks': boxing_rev_list[2], 'Sales': boxing_rev_list[3], 'Revenue': boxing_rev_list[4], 'Revenue(est)': boxing_rev_list[5]}
boxing_rev = pd.DataFrame(boxing_rev_dict)


boxing_df.to_excel('Excel Sheets/Boxing PPV.xlsx', index=False)