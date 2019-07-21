'''
Created on Jul 21, 2019
'''
import pandas as pd

df = None
sheet = "Multiple"

def getConditionFromDrug(drugName): #returns first matching row to the drug. returns message if no condition found
    global df
    try:
        obj = df[df["drugName"] == drugName].iloc[0]
        return obj.condition
    except IndexError:
        return "No condition found"
    
def groupbyCondition(condition):
    global df
    filteredDF = df[df["condition"] == condition]
    groupedDF = filteredDF.groupby("drugName")["usefulCount","review_classification"].agg(list)
#     print(groupedDF)
    for name in groupedDF.index:
        print("\n",name)
        print(groupedDF.loc[name]["usefulCount"])
        print(groupedDF.loc[name]["review_classification"])
    
        
def initSearch(drugName):
    global df
    df = pd.read_excel("trained_dataset.xlsx",sheet_name=sheet)
    condition = getConditionFromDrug(drugName)
    groupbyCondition(condition)

initSearch("Saxenda")