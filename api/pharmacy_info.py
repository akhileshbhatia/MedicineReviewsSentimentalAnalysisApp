'''
Created on Jul 28, 2019
'''
import mysql.connector

def createConnection():
    try:
        connection = mysql.connector.connect(host="127.0.0.1", database="thesis_ucc",user="root",password="")
        return connection
    except:
        return "Something went wrong while connecting to database"


def getPharmaciesHavingDrug(drugName):
    returnValue = {}
    connection = createConnection()
    if connection == "Something went wrong while connecting to database":
        returnValue["error"] = connection
        return returnValue
    
    cursor = connection.cursor()
    cursor.execute("SELECT pharmacy.name,pharmacy.latitude as lat,pharmacy.longitude as lng,info.quantity from pharmacy\
    INNER JOIN pharmacy_drug info ON pharmacy.id = info.pharmacy_id\
    INNER JOIN drug ON info.drug_id = drug.id \
    WHERE drug.name = '"+drugName+"'")
    rowHeaders = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    connection.close()
    if len(data) == 0:
        return "No such drug exists"
    else:
        details = []
        for result in data:
            obj = dict(zip(rowHeaders,result))
            details.append(obj)
        returnValue["details"] = details
        return returnValue
# print(getPharmaciesHavingDrug("Duloxetine"))
