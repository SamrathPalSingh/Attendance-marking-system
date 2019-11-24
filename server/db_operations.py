import sqlite3

def checkRecord(name, rollnum, mac):
    db = sqlite3.connect('C:/Users/Tintin/Documents/software_project/server/alldata.db')
    try:
        cursor = db.execute("SELECT * FROM STUDENT WHERE NAME= '" + str(name) + "' and ROLLNUM= " + str(rollnum) + " and MAC= '" + str(mac) + "';")
        print(cursor)
        data = cursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return True
    except:
        return False

def addToError(name , rollnum):
    db = sqlite3.connect('C:/Users/Tintin/Documents/software_project/server/alldata.db')
    try:
        db.execute("INSERT INTO ERRORS(NAME, ROLLNUM) VALUES('" + str(name) + "', "+ str(rollnum) +");")
        db.execute("commit;")
    except:
        print("ERROR! RECORD NOT ADDED TO DB")
def getErrorEnteries():
    db = sqlite3.connect('C:/Users/Tintin/Documents/software_project/server/alldata.db')
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM ERRORS;")
        result = cur.fetchall()
        print(result[0][0])
        return (result)
    except:
        print("ERROR! RECORD NOT ADDED TO DB")
    result = []
    return (result)
def deleteErrorsTable():
    db = sqlite3.connect('C:/Users/Tintin/Documents/software_project/server/alldata.db')
    try:
        db.execute("delete from errors;")
        db.execute("commit;")
    except:
        print("ERROR! RECORD NOT ADDED TO DB")