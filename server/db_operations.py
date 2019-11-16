import sqlite3

def checkRecord(name, rollnum, mac):
    db = sqlite3.connect('alldata.db')
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


def markAttendance(name, rollnum):
    pass

def addToError(name , rollnum):
    db = sqlite3.connect('alldata.db')
    try:
        db.execute("INSERT INTO ERRORS(NAME, ROLLNUM) VALUES('" + str(name) + "', "+ str(rollnum) +");")
        db.execute("commit;")
    except:
        print("ERROR! RECORD NOT ADDED TO DB")
