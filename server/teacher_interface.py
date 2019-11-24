from tkinter import *
from tkinter import filedialog
import threading
import db_operations as dbo
import time
import os
import server
import pandas as pd
import csv
from datetime import date
global mylist
global refresh
global thread
global df
def makeNewEntry(): 
    global df
    today = date.today()
    df=pd.read_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\Book1.csv')
    #print((df.columns)[-1])
    #print(today)
    if( str((df.columns)[-1]) != str(today) ):
        df[str(today)]= ['a' for i in range(len(df.index))]#only for 3 three students
        #df.set_index("roll",inplace=True)
        #print(lastDate)
        #print(df.head())
        #df.to_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv')

def markattendance(rollnum):
    global df
    df=pd.read_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv')
    today = date.today()
    makeNewEntry()
    row = len(df.index)
    for i in range(0,row+1):
        #print(df.head())
        if( str(df.at[i,'roll']) == str(rollnum) ):
            df.at[i,str(today)]='p'
            break 
    df.to_csv('C:\\Users\\Tintin\\Documents\\software_project\\server\\Book1.csv', index=False)

root = Tk()
actionButton = StringVar()
actionButton=StringVar()
actionButton.set('Start Server')
refreshButton = StringVar()
refreshButton.set('Refresh List')
mark= StringVar()
mark.set('Mark Attendance')
def markFunc():
    global mylist
    values = [mylist.get(idx) for idx in mylist.curselection()]
    print(values)
    #result=dbo.getErrorEnteries()
    #files = []
    for f in values:
        f=f.split('(')[1]
        f=f[:-1]
        print(f)
        markattendance(f)
def refreshFunc():
    global mylist
    global files
    result=dbo.getErrorEnteries()
    files = []
    for f in result:
        files.append(str(f[0]) + ' (' + str(f[1]) + ')' )
    mylist.delete(0, END)
    i=1
    for f in files:
        mylist.insert(i, f)
        i=i+1
def serve():
    #os.popen('C:/Users/Tintin/AppData/Local/Programs/Python/Python37-32/python.exe c:/Users/Tintin/Documents/software_project/server/server.py')
    server.runMe()
def startServer():
    global actionButton
    global refresh
    global mylist
    global thread
    if str(actionButton.get()) == 'Start Server':
        actionButton.set("Stop Server")
        ss2.grid(row=2)
        ss3.grid(row=3)
        refreshFunc()
        thread=threading.Thread(target=serve, args=[])
        thread.start()
    else:
        actionButton.set("Start Server")
        ss2.grid_remove()
        ss3.grid_remove()
        dbo.deleteErrorsTable()
        #thread.join()

#frame for server setup
ss0 = Frame(root)
ss0.pack(side = TOP)
ss = Frame(ss0)
ss.grid(row=1)
#buttonLabel= Label(ss, text='Select the folder you want to set up as a Server', relief=FLAT, padx=5, pady=5)
#buttonLabel.grid(row=1, column=1)
start = Button(ss, textvariable=actionButton, command=startServer)
#folderLocation=Button(ss, text='Browse', command=startServer)
#folderLocation.grid(row=1, column=2)
start.grid(row=1)
ss2 = Frame(ss0)
#ss2.grid(row=2)
scrollbar = Scrollbar(ss2)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(ss2, yscrollcommand = scrollbar.set, selectmode=EXTENDED, width=60 )
mylist.pack( side = LEFT, fill = BOTH)
scrollbar.config( command = mylist.yview )
i=1
files = ["one", "two", "three"]
for f in files:
    mylist.insert(i, f)
    i=i+1
ss3 = Frame(ss0)
#ss3.grid(row=3)
refresh = Button(ss3, textvariable=refreshButton, command=refreshFunc)
refresh.grid(row=1, column=1)
markAttendance = Button(ss3, textvariable=mark, command=markFunc) 
markAttendance.grid(row=1, column=2)
#global mylist
# folderLabel=Label(ss2, textvariable="folder", relief=FLAT)
# folderLabel.grid(row=1, column=1)
# ss3 = Frame(ss0)
# ss3.grid(row=3)
# portLabel= Label(ss3, text='Enter port number', relief=FLAT, padx=5, pady=5)
# portLabel.grid(row=1, column=1)
# global portEntry
# portEntry=Entry(ss3)
# portEntry.grid(row=1, column=2)
# ss4 = Frame(ss0)
# ss4.grid(row=4)
# start = Button(ss4, textvariable="actionbutton", command=startServer)
# start.grid(row=1, column=1)
# ss5=Frame(ss0)
# ss5.grid(row=5)
# connectionStatus = Label(ss5, textvariable="connectionStatusFlag", relief=FLAT, padx=5, pady=5)
# connectionStatus.grid(row=1, column=1)
# ss6=Frame(ss0)
# ss6.grid(row=6)
# credentials = Label(ss6, textvariable="credentialsFlag", relief=FLAT, padx=5, pady=5)
# credentials.grid(row=1, column=1)#ADD data into this label
root.title('Teacher Interface')
root.geometry('450x450')
root.mainloop()