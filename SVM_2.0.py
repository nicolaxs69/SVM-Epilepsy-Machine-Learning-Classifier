import pandas as pd
import numpy as np
import csv

'''
Author: Nicolas Escobar Cruz
Date : 9/08/2017

The following code consists of the training of an SVM classifier using the scientific libraries of Scikit-learn and Scipy among others.
This classifier aims to predict whether a patient is suffering from a seizure triggered by an epilepsy attack.

For this version was made the construction of a dataset which contains information about two subjects walking, running and simulating a convulsion.
The dataset together with the respective files are inside the root folder of the program.
'''


'''
First Step: Load the dataset

A CSV file is loaded which contains the dataset that was constructed from the following activities: 
Walking, Running, Convulsing this information was recorded by an accelerometer.

For each recording, a 10 sg window was extracted from which the following 4 characteristics were extracted: 
maximum, minimum, mean and variance. In order to pass them to the SVM.
'''
column = []
source = open("Dataset\SMV\Features_raw_1.csv")
csv_f = csv.reader(source)
for row in csv_f:
    column.append(row[3]) # Select the Feature Column from the CSV File
    results = list(map(int, [i.replace(".", "") for i in column]))  # [['511.136.820.926'], ['578.468.812.877']] = [[511136820926], [578468812877]]
    array = np.vstack(results) #np.vstack = [[1][2][3]]
    X = array.tolist()         #tolist() = [[1],[2],[3]]
source.close()
print(X)


# # Using the Pandas and Numpy Libraries
# file = pd.read_csv("Dataset\SMV\Features_raw.csv", sep = ',')
# #A = np.array(file[["maximo", "minimo","media"]])
# A = np.array(file[["media"]]).tolist()
# print(A)

# _______________________________________________________Support Vector Machine Training__________________________________________________________________
from sklearn import svm
from sklearn import metrics

#Input Data to evaluate by the SVM, here the incoming 10 sg dataframe by the bitalino are proccesed contunuosly.
#target =[860,286, 0.33411033,97347542 ]
target =[900]


#Load the categories for the SVM
categories= "Dataset\SMV\Categories.txt"
lista = [line.rstrip('\n') for line in open(categories)]
categorias = [int(x) for x in lista]  # String to Int

y = categorias # Category:  0 - Seizure , 1 - Walk, 2 - Running
# Load the SVM kernel , type Linear SVC
clf = svm.SVC()
# Learning of the SVM
clf.fit(X, y)
# Prediction of the target
res= clf.predict(target)

print(res)

if res == 0:
    print("SE DETECTO CONVULSION")
if res == 1 :
    print("SE DETECTO CAMINANDO")
if res == 2:
        print("SE DETECTO CORRIENDO")
