'''
Created on Jul 28, 2019
'''
import mysql.connector
from mysql.connector import errorcode

connection = None
# data = None
try:
    connection = mysql.connector.connect(host="127.0.0.1", database="thesis_project_ucc",user="root",password="")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        data = "Access denied to selected database"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        data = "Database doesn't exist"
    else:
        data = err

def getPharmaciesHavingDrug(drugName):
#     global data
    if connection != None and connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT store.*, info.quantity, drug.condition_name from store\
        INNER JOIN store_drug_info info ON store.store_id = info.store_id\
        INNER JOIN drug ON info.drug_id = drug.drug_id\
        WHERE drug.drug_name = '"+drugName+"' \
        ORDER by drug.condition_name, info.quantity DESC")
        rowHeaders = [x[0] for x in cursor.description]
        data = cursor.fetchall()
        jsonData = []
        conditionInfo = {}
        if len(data) == 0:
            data = "No such drug exists"
        else:
            for result in data:
                infoObj = dict(zip(rowHeaders,result))
                condition = infoObj["condition_name"] 
                if condition in conditionInfo:
                    conditionInfo[condition] += 1
                else:
                    conditionInfo[condition] = 1
                jsonData.append(infoObj)
            jsonData.insert(0, conditionInfo)
            return jsonData
    return data

# print(getPharmaciesHavingDrug("Duloxetine"))
