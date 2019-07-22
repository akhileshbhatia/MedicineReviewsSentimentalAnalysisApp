'''
Created on Jul 21, 2019
'''
import pandas as pd
import common_utilities as cu
import time

def getConditionFromDrug(drugName): #returns first matching row to the drug. returns message if no condition found
    global df
    try:
        obj = df[df["drugName"] == drugName].iloc[0]
        return obj.condition
    except IndexError:
        return ""
    
def getGroupedDataframeByCondition(condition): #returns the usefulCount
    global df
    filteredDF = df[df["condition"] == condition]
    return filteredDF.groupby("drugName")["usefulCount","review_classification","date_weights"].agg(list)
    
        
def getAlternatives(drugName):
    global df
    condition = getConditionFromDrug(drugName)
    if condition != "":
        groupedDF = getGroupedDataframeByCondition(condition)
        return getRanking(groupedDF)
    else:
        return "Drug not found"

def getRanking(groupedDF):
    classificationMap = cu.getReviewClassificationWeights()
    alternativeWithScores = {}
    for drugName in groupedDF.index:
        alternativeWithScores[drugName] = 0.0
        usefulCount = groupedDF.loc[drugName]["usefulCount"]
        reviewClassification = groupedDF.loc[drugName]["review_classification"]
        dateWeights = groupedDF.loc[drugName]["date_weights"] 
        for i in range(len(dateWeights)):
            alternativeWithScores[drugName] += usefulCount[i] * classificationMap.get(reviewClassification[i]) * dateWeights[i]
    
    
    for data in sorted(alternativeWithScores.items(), key = lambda x : x[1], reverse = True):
        print("\n",data)
        getDrugClassificationDetails(data[0])

def getDrugClassificationDetails(drugName):        
    global df
    filteredDF = df[df["drugName"] == drugName]

    printDetails(filteredDF, "Excellent")
    printDetails(filteredDF, "Good")
    printDetails(filteredDF, "Average")
    printDetails(filteredDF, "Poor")
    
def printDetails(filteredDF,reviewType):
    newDF = filteredDF[filteredDF["review_classification"] == reviewType]
    length = len(newDF.index)
    print(reviewType, " => ", length)
    if length > 0:
        sortedDF = newDF.sort_values(by="date",ascending=False,inplace=False)
        dateStrings = [d.strftime("%d-%m-%Y") for d in sortedDF.date.tolist()]
        print(dateStrings)
        print("Sum of useful count => ", sum(sortedDF.usefulCount.tolist()))
          
start_time = time.time()
sheet = cu.getSheetName()
df = pd.read_excel("trained_dataset.xlsx",sheet_name=sheet)            
getAlternatives("Duloxetine")
print("\n\nTime taken => ", time.time() - start_time)