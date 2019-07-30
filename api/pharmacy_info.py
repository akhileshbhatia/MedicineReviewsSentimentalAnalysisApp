'''
Created on Jul 28, 2019
'''
import mysql.connector

def createConnection():
    try:
        connection = mysql.connector.connect(host="127.0.0.1", database="thesis_project_ucc",user="root",password="")
        return connection
    except:
        return "Something went wrong while connecting to database"

def postProcessRawData(rawData): 
    return None
def getPharmaciesHavingDrug(drugName):
    returnValue = {}
    connection = createConnection()
    if connection == "Something went wrong while connecting to database":
        returnValue["info"] = connection
        return returnValue
    
    cursor = connection.cursor()
    cursor.execute("SELECT store.name,store.latitude,store.longitude,info.quantity, drug.condition_name from store\
    INNER JOIN store_drug_info info ON store.store_id = info.store_id\
    INNER JOIN drug ON info.drug_id = drug.drug_id \
    WHERE drug.drug_name = '"+drugName+"' \
    ORDER by drug.condition_name, info.quantity DESC")
    rowHeaders = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    if len(data) == 0:
        return "No such drug exists"
    else:
        rawData = {}
        detailsList = []
        conditionInfo = {}
        for result in data:
            obj = dict(zip(rowHeaders,result))
            condition = obj["condition_name"] 
            if condition in conditionInfo:
                conditionInfo[condition] += 1
            else:
                conditionInfo[condition] = 1
            detailsList.append(obj)
        
        return postProcessRawData(rawData)
    connection.close()
# print(getPharmaciesHavingDrug("Duloxetine"))
