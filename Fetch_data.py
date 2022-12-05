import requests
import datetime
from datetime import timedelta
import pandas as pd
from urllib.request import urlopen
import os
from zipfile import ZipFile
  

# Helper Functions
def get_month(m):
    if(m==1):
        month = "JAN"
    if(m==2):
        month = "FEB"
    if(m==3):
        month = "MAR"
    if(m==4):
        month = "APR"
    if(m==5):
        month = "MAY"
    if(m==6):
        month = "JUN"
    if(m==7):
        month = "JUL"
    if(m==8):
        month = "AUG"
    if(m==9):
        month = "SEP"
    if(m==10):
        month = "OCT"
    if(m==11):
        month = "NOV"
    if(m==12):
        month = "DEC"
    return month


# 1. TO  Programatically fetch “Securities available for Equity segment (.csv)” file
url1 = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
df = pd.read_csv(url1)
df.to_csv('fSecurties.csv')
print("Program 1 FInished!!")

# 2. Programatically get the latest “bhavcopy” csv file
today = datetime.datetime.now()
today = today -timedelta(days=1)
yr = str(today.year)
m = today.month
month=get_month(m)
# print(today.day)
d = '{:02d}'.format(today.day)
d = str(d)
current_date = d+month+yr
# print(today)
url2 = 'https://archives.nseindia.com/content/historical/EQUITIES/2022/'+f"{month}"+'/cm'+f"{current_date}"+'bhav.csv.zip'
r = requests.head(url2)
if r.status_code == 503:
    # print(f'{url2} was found')
    df = pd.read_csv(url2)
    df.to_csv('bhavcopies.csv')
# https://archives.nseindia.com/content/historical/EQUITIES/2022/DEC/cm02DEC2022bhav.csv.zip
print("Program 2 FInished!!")
# load the data into a Pandas DataFrame
merged = pd.read_csv('bhavcopies.csv').merge(pd.read_csv('fSecurties.csv'),on=["SYMBOL"])
merged.drop("Unnamed: 0_x",inplace=True,axis=1)
merged.drop("Unnamed: 0_y",inplace=True,axis=1)
merged.drop("Unnamed: 13",inplace=True,axis=1)
merged.to_csv('New_File.csv')
print("Program 3 FInished!!")


# 4. In addition to step 2, programmatically get BHAvcopies of the last 30 days instead of just the latest one.
today1 = datetime.datetime.now()
today1 = today1 - timedelta(days=1) 
# DOne as 3dec file is still not available
dt = datetime.datetime.now()
dt = dt - timedelta(days=1) 
count = 1
i = 0
while 1:
    yesterday = today1 - timedelta(days=i)
    dt = today - timedelta(days=i)
    i+=1
    
    x = dt.weekday()
    # print(x)
    yr = str(yesterday.year)
    m = yesterday.month
    month=get_month(m)
    d = '{:02d}'.format(yesterday.day)
    d = str(d)
    if x==5 or x==6:   
        continue
    if d=='00':
        continue
    current_date = d+month+yr
    if current_date == '08NOV2022' :
        continue
    if current_date == '26OCT2022' :
        continue 
    # print(current_date)
    
    url2 = 'https://archives.nseindia.com/content/historical/EQUITIES/2022/'+f"{month}"+'/cm'+f"{current_date}"+'bhav.csv.zip'
    r = requests.get(url2)
    # print(url2)
    # print(r.status_code)
    if r.status_code == 200:
        # print(f'{url2} was found')
        df = pd.read_csv(url2)
        count+=1
        df.to_csv('bhavcopies'+f"{count}"+'.csv')
        
    if count ==30:
        break
    # print(count)
print("Program 4 FInished!!")    
