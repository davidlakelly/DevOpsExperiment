#https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/DATASET_CODE?lang=EN

import sys
import requests
sys.stdout = open("test1.CSV", "w")
r = requests.get('https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tps00019?lang=EN')
print(r.json())


#sys.stdout = open('C:\Users\Emlyn Farrell\DevOpsExperiment\output, 'output')

#sys.stdout.close()


#$ python script.py > C:\Users\Emlyn Farrell\DevOpsExperiment\

#python script.py > DevOpsExperiment\


#sys.stdout = python3 script.py | tee output.txt

#sys.stdout = open("test.txt", "w")
sys.stdout.close()