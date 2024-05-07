#https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/DATASET_CODE?lang=EN

import sys
import requests
import csv
import pandas as pd
import sqlite3



#query to get data from the site
def get_data():
    r = requests.get('https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tps00019?lang=EN')
    df = pd.read_json(r.json())
    
    #return r.json()
    return  r.json()
 
 
#DB stuff

#con = sqlite3.connect("DevOpsTest.db")

# connects to DB but doesnt see table
#df = pd.read_sql_query("SELECT * from Data", con)
#Json to Dataframe








#print(df.to_string())

#sys.stdout = open('C:\Users\Emlyn Farrell\DevOpsExperiment\r.json', 'w')
#sys.stdout.close()





#with open("TestData.csv", 'r') as file:
#  csvreader = csv.reader(file)
#  for row in csvreader:
#    print(row)

#save data in a panda DF
#data = pd.read_csv("TestData.csv")
#data





#print(r.json())

#f = open("test1.CSV", "w")

#open the csv file and provide a variable
#with open("test1.CSV", "w") as f:


#print("Hello World")
#r = requests.get('https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tps00019?lang=EN')
#print(r.json())


#sys.stdout = open('C:\Users\Emlyn Farrell\DevOpsExperiment\output, 'output')

#sys.stdout.close()


#$ python script.py > C:\Users\Emlyn Farrell\DevOpsExperiment\

#python script.py > DevOpsExperiment\


#sys.stdout = python3 script.py | tee output.txt

#sys.stdout = open("test.txt", "w")
#sys.stdout.close()