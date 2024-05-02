#https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/DATASET_CODE?lang=EN

import sys
import requests

def get_data():
    r = requests.get('https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tps00019?lang=EN')
    return r.json()
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