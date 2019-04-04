import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def pl_statement(inp):
    bal_sheet = pd.DataFrame()
    driver = webdriver.Chrome(r"path")
    driver.get("https://www.google.com/")
    driver.find_element_by_name('q').send_keys("https://www.moneycontrol.com/financials/"+inp.replace(" ", "")+"/profit-lossVI/")
    webelem = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[2]/div/div[3]/center/input[2]')
    webelem.click()
    sym = driver.find_element(By.XPATH, '//*[@id="nChrtPrc"]/div[1]').text
    symbol = []
    i1 = 17
    while sym[i1] != '|':
        symbol.append(sym[i1]);
        i1 = i1 + 1
    sym = ''.join(symbol)
    x=0
    while x<54:
        test=driver.find_element(By.XPATH,'//*[@id="mc_mainWrapper"]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[2]/tbody/tr['+str(x+7)+']').text
        if test=="" :
            break
        y=0
        string=driver.find_element(By.XPATH, '//*[@id="mc_mainWrapper"]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[2]/tbody/tr['+str(x+7)+']/td['+str(y+1)+']').text
        if re.match( '[A-Z][A-Z][a-zA-Z]+', string ):
            pass
        else:
            while y<=5:
                bal_sheet.loc[x,y]=driver.find_element(By.XPATH, '//*[@id="mc_mainWrapper"]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[2]/tbody/tr['+str(x+7)+']/td['+str(y+1)+']').text
                y=y+1
        x=x+1
    bal_sheet.set_index(0,inplace=True)
    print(bal_sheet.to_string())
    e1=float(bal_sheet[1]['Total Expenses'].replace(',', ''))  #expense
    e2=float(bal_sheet[2]['Total Expenses'].replace(',', ''))
    e3=float(bal_sheet[3]['Total Expenses'].replace(',', ''))
    e4=float(bal_sheet[4]['Total Expenses'].replace(',', ''))
    e5=float(bal_sheet[5]['Total Expenses'].replace(',', ''))
    r1=float(bal_sheet[1]['Total Revenue'].replace(',', ''))   #revenue
    r2=float(bal_sheet[2]['Total Revenue'].replace(',', ''))
    r3=float(bal_sheet[3]['Total Revenue'].replace(',', ''))
    r4=float(bal_sheet[4]['Total Revenue'].replace(',', ''))
    r5=float(bal_sheet[5]['Total Revenue'].replace(',', ''))
    gr1=(r5-r4)/r5       #growth rate
    gr2=(r4-r3)/r4
    gr3=(r3-r2)/r3
    gr4=(r2-r1)/r2
    agr=(gr1+gr2+gr3+gr4)/4
    assumed_r=r1+r1*agr   #assumed revenuue
    assumed_e=(e1+e2+e3+e4+e5)/5    #assumed expense
    decide=assumed_r-assumed_e

    if(decide>=0):
        print("According to the Profit-loss statement this company is profitable")
    else:
        print("According to the Profit-loss statement this company is not profitable")
    return sym
