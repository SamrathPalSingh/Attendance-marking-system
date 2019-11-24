import pandas as pd
import csv

def markattendance(rollnum,date):
    df.at[rollnum,date]="p"
rollnum=input("Enter the rollnumber :")
rollnum=int(rollnum)

df=pd.read_csv('C:\\Users\\Tintin\\Downloads\\b.csv')
from datetime import date
today = date.today()
df[today]= ['a' for i in range(3)]
df.set_index("roll",inplace=True)
print(df.head())

markattendance(rollnum,today)
df.to_csv('C:\\Users\\Tintin\\Downloads\\b.csv')
print(df.head())