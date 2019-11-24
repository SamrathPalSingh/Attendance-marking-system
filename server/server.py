from flask import Flask, render_template, flash
import forms
import db_operations as dbo
import pandas as pd
import csv
from datetime import date
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bfb9f13102dc4c807e14ed5975a1471d'
global df
df=pd.read_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv')
def makeNewEntry(): 
    global df
    today = date.today()
    df=pd.read_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv')
    print((df.columns)[-1])
    print(today)
    if( str((df.columns)[-1]) != str(today) ):
        df[str(today)]= ['a' for i in range(len(df.index)) ]#only for 3 three students
        #df.set_index("roll",inplace=True)
        #print(lastDate)
        print(df.head())
        #df.to_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv')

def markattendance(rollnum):
    global df
    today = date.today()
    makeNewEntry()
    row = len(df.index)
    for i in range(0,row+1):
        print(df.head())
        if( str(df.at[i,'roll']) == str(rollnum) ):
            df.at[i,str(today)]='p'
            break 
    df.to_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv', index=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.MarkAttendance()
    if form.validate_on_submit():
        flag= dbo.checkRecord( str(form.name.data), str(form.rollnum.data), str(form.mac.data) )
        #print(flag)
        if(flag):
            markattendance( str(form.rollnum.data) )
            return ("Verified")
        else:
            #remember to clear the error table everytime the teacher interface is booted
            dbo.addToError(str(form.name.data), str(form.rollnum.data))
            return("Not Verified")
    return (render_template('index.html', form=form))

def runMe():
    app.debug=False
    app.run()
if __name__ == '__main__':
    app.debug=False
    app.run()