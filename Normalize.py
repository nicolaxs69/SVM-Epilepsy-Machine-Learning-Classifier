import pandas as pd
import numpy as np
from sklearn import preprocessing
import csv

# df = pd.io.parsers.read_csv(
#     'Dataset\SMV\Raw_csv.csv',
#      header=None)
#df.columns=['maximo', 'minimo','media','varianza']

raw = pd.read_csv('Dataset\SMV\Features_raw.csv', header=0)

csvFileArray = []
for row in csv.reader(raw, delimiter=','):
    csvFileArray.append(row)

#print()
#print(csvFileArray[2])
#print(raw.loc[:34,'media'])
print(raw.loc[:,:])



maximo = list(raw.maximo)
minimo= list(raw.minimo)
media= list(raw.media)
varianza =list(raw.varianza)
print(media)
sin = list(map(int, [i.replace(".", "") for i in varianza]))

#print(maximo)
X_normalized = preprocessing.normalize(sin, norm='max')
#rint(X_normalized)

#maximo = np.max(maximo)
#minimo = np.min(data)
#media  = np.mean(sin)
#varianza = np.var(data)
#
#print(X_normalized)
#print ("Maximo:",maximo)
#print ("Minimo:",minimo)
#print ("Media:", media)
#print("Varianza:",varianza)


# Define Data
string =  list(map(str,(sin)))
# RESULTS =  string
#
#
# # Open File
# resultFyle = open("output.csv",'w')
#
# # Write data to file
# for r in RESULTS:
#     resultFyle.write(r + "\n")
# resultFyle.close()
