'''
Created on Jun 10, 2019

@author: akhilesh
'''
import pymysql
import pandas as pd

''' reading the excel file'''
df = pd.read_excel("drug_condition.xlsx")

'''connect to database and get cursor'''
con = pymysql.connect("localhost","root","","thesis_project_ucc")
cursor = con.cursor()
'''creating insert statement'''
query = "INSERT INTO `drug_condition`(`drug_name`,`condition_name`) VALUES (%s, %s)"
for index,row in df.iterrows():
    drugName = row['drugName']
    condition = row['condition']
    
    values = (drugName,condition)
    
    cursor.execute(query,values)

cursor.close()

con.commit()

con.close()

print("Finished");

    
    