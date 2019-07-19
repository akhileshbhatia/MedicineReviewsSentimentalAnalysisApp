'''
Created on Jul 19, 2019
'''
import pandas as pd
from _datetime import datetime
import os.path
import time

def assignWeight():
    
    
    fileName = "trained_dataset.xlsx"
       
    #check if file exists
    if not os.path.isfile(fileName):
        return "Trained dataset file not found"
    
    #assuming that the sheet would exist
    f = open("weight_assignment_log.txt", "a")
    start_time = time.time(); 
    today = datetime.today()
    f.write("\n-------------------------------------------------")
    f.write("\nRequest to assign weight to dates started on "+ str(today))
    
    sheet = "Multiple"
    df = pd.read_excel(fileName,sheet_name=sheet) 
    df.sort_values(by="date",ascending=False,inplace=True)
    
    daysDiff = []
    inverseDaysDiff = []
    sumOfInverseDaysDiff = 0
    
    for index,row in df.iterrows():
        diff = (today - row["date"]).days
        daysDiff.append(diff)
        inverse = float(("{0:6f}".format(1/diff)))
        inverseDaysDiff.append(inverse)
        sumOfInverseDaysDiff += inverse
    
    
    weightedDays = [float(("{0:.6f}".format(x/sumOfInverseDaysDiff))) for x in inverseDaysDiff]
    
    f.write("\nWeight calculation done for the sheet "+sheet)
    
    df["dateWeights"] = weightedDays
    
    df.to_excel(fileName,sheet_name=sheet,index=False)
    
    f.write("\nWeight saved to file")
    
    f.write("\nWeight calculation completed in " + str("{0:.2f}".format(time.time() - start_time)) +" seconds")
    
    f.close()
    
    return "Weight assignment complete"

    

