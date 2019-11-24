from datetime import date
import pandas as pd
global df
df=pd.read_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv')

def makeNewEntry(): 
    global df
    today = date.today()
    print((df.columns)[-1])
    print(today)
    if( str((df.columns)[-1]) != str(today) ):
        df[str(today)]= ['a' for i in range(3)]#only for 3 three students
        # df.set_index("roll",inplace=True)
        #print(lastDate)
        print(df.head())                                                                                                                                                
        #df.to_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv')


today = date.today()
makeNewEntry()
print('----')
print(df.head())
print('----')
row = len(df.index)
for i in range(0,row+1):
    print(df.head())
    if( str(df.at[i,'roll']) == str('101703491') ):
        df.at[i,str(today)]='p'
        break 
df.to_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv', index=False)