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


# 2. Programatically get the latest “bhavcopy” csv file
today = datetime.datetime.now()
yr = str(today.year)
m = today.month
month=get_month(m)
d = str(today.day)
# print(d)
# print(f"{d}{month}{yr}")
current_date = d+month+yr
url2 = 'https://archives.nseindia.com/content/historical/EQUITIES/2022/NOV/'+'cm'+f"{current_date}"+'bhav.csv.zip'
df = pd.read_csv(url2)
df.to_csv('bhavcopies.csv')



# load the data into a Pandas DataFrame
merged = pd.read_csv('bhavcopies.csv').merge(pd.read_csv('fSecurties.csv'),on=["SYMBOL"])
merged.drop("Unnamed: 0_x",inplace=True,axis=1)
merged.drop("Unnamed: 0_y",inplace=True,axis=1)
merged.drop("Unnamed: 13",inplace=True,axis=1)
merged.to_csv('New_File.csv')



# 4. In addition to step 2, programmatically get BHAvcopies of the last 30 days instead of just the latest one.
today1 = datetime.datetime.now()
dt = datetime.datetime.now()

for i in range(30):
    yesterday = today1 - timedelta(days=i)
    dt = today - timedelta(days=i)
    x = dt.weekday()
    yr = str(yesterday.year)
    m = yesterday.month
    month=get_month(m)
    d = str(yesterday.day)
    if x==5 or x==6:   
        continue
    if d=='0':
        continue
    current_date = d+month+yr
    print(current_date)
    url2 = 'https://archives.nseindia.com/content/historical/EQUITIES/2022/NOV/'+'cm'+f"{current_date}"+'bhav.csv.zip'
    df = pd.read_csv(url2)
    df.to_csv('bhavcopies'+f"{i}"+'.csv')
