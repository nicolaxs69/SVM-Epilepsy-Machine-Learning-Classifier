from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Datasets:
# Seizure:
seizure_1 = "Dataset\Corriendo\Corriendo_Suj-1_#1.txt"
seizure_2 = "Dataset\Caminando\Daianara_caminando.txt"
seizure_3 = "Dataset\Caminando\Abuelo_Nicolas_Caminando.txt"
seizure_4 = "Dataset\Caminando\Carlos_Caminando.txt"
seizure_5 = "Dataset\Convulsion\Convulsion_Test.txt"

lista = [line.rstrip('\n') for line in open(seizure_5)]
data = [int(x) for x in lista]  # String to Int

# Seizure Training Dataset

array1 = data[0:1491];
array2 = data[1491:2982];
array3 = data[2982:4473];
array4 = data[4473:5964];
array5 = data[5964:7455];
array6 = data[7455:8946];
array7 = data[8946:10437];
array8 = data[10437:11928];
array9 = data[11928:13419];
array10 = data[13419:14910];
array11 = data[14910:16401];
array12 = data[16401:17895];
array13 = data[17895:19836];
array14 = data[19836:20877];
array15 = data[20877:22368];
array16 = data[22368:23859];
array17 = data[22368:25350];
array18 = data[25350:26841];
array19 = data[26841:28332];
array20 = data[28332:29823];
array21 = data[29823:31314];

#print(array1)

data = array1
maximo = np.max(data)
minimo = np.min(data)
media = np.mean(data)
varianza = np.var(data)

# a = "Maximo:", maximo
# b = "Minimo:", minimo
# c = "Media:", media
# d = "Varianza:", varianza
#
# print ("Maximo:",maximo)
# print ("Minimo:",minimo)
# print ("Media:", media)
# print("Varianza:",varianza)


#_____________________________________________________________________________________
# Print a row from the CSV dataset file
csvfile = open('Dataset\SMV\Standar.csv', 'r')
csvFileArray = []
for row in csv.reader(csvfile, delimiter=';'):
    csvFileArray.append(row)

arra1 = list(map(int, [i.replace(".", "") for i in csvFileArray[1]]))
arra2 = list(map(int, [i.replace(".", "") for i in csvFileArray[2]]))
arra3 = list(map(int, [i.replace(".", "") for i in csvFileArray[3]]))
arra4 = list(map(int, [i.replace(".", "") for i in csvFileArray[4]]))
arra5 = list(map(int, [i.replace(".", "") for i in csvFileArray[5]]))
arra6 = list(map(int, [i.replace(".", "") for i in csvFileArray[6]]))
arra7 = list(map(int, [i.replace(".", "") for i in csvFileArray[7]]))
arra8 = list(map(int, [i.replace(".", "") for i in csvFileArray[8]]))
arra9 = list(map(int, [i.replace(".", "") for i in csvFileArray[9]]))
arra10 = list(map(int, [i.replace(".", "") for i in csvFileArray[10]]))
arra11 = list(map(int, [i.replace(".", "") for i in csvFileArray[11]]))
arra12 = list(map(int, [i.replace(".", "") for i in csvFileArray[12]]))
arra13 = list(map(int, [i.replace(".", "") for i in csvFileArray[13]]))
arra14 = list(map(int, [i.replace(".", "") for i in csvFileArray[14]]))
arra15 = list(map(int, [i.replace(".", "") for i in csvFileArray[15]]))
arra16 = list(map(int, [i.replace(".", "") for i in csvFileArray[16]]))
arra17 = list(map(int, [i.replace(".", "") for i in csvFileArray[17]]))
arra18 = list(map(int, [i.replace(".", "") for i in csvFileArray[18]]))
arra19 = list(map(int, [i.replace(".", "") for i in csvFileArray[19]]))
arra20 = list(map(int, [i.replace(".", "") for i in csvFileArray[20]]))
arra21 = list(map(int, [i.replace(".", "") for i in csvFileArray[21]]))
arra22 = list(map(int, [i.replace(".", "") for i in csvFileArray[22]]))
arra23 = list(map(int, [i.replace(".", "") for i in csvFileArray[23]]))
arra24 = list(map(int, [i.replace(".", "") for i in csvFileArray[24]]))
arra25 = list(map(int, [i.replace(".", "") for i in csvFileArray[25]]))
arra26 = list(map(int, [i.replace(".", "") for i in csvFileArray[26]]))
arra27 = list(map(int, [i.replace(".", "") for i in csvFileArray[27]]))
arra28 = list(map(int, [i.replace(".", "") for i in csvFileArray[28]]))
arra29 = list(map(int, [i.replace(".", "") for i in csvFileArray[29]]))
arra30 = list(map(int, [i.replace(".", "") for i in csvFileArray[30]]))
arra31 = list(map(int, [i.replace(".", "") for i in csvFileArray[31]]))
arra32 = list(map(int, [i.replace(".", "") for i in csvFileArray[32]]))
arra33 = list(map(int, [i.replace(".", "") for i in csvFileArray[33]]))
arra34 = list(map(int, [i.replace(".", "") for i in csvFileArray[34]]))
arra35 = list(map(int, [i.replace(".", "") for i in csvFileArray[35]]))
arra36 = list(map(int, [i.replace(".", "") for i in csvFileArray[36]]))
arra37 = list(map(int, [i.replace(".", "") for i in csvFileArray[37]]))
arra38 = list(map(int, [i.replace(".", "") for i in csvFileArray[38]]))
arra39 = list(map(int, [i.replace(".", "") for i in csvFileArray[39]]))
arra40 = list(map(int, [i.replace(".", "") for i in csvFileArray[40]]))
arra41 = list(map(int, [i.replace(".", "") for i in csvFileArray[41]]))
arra42 = list(map(int, [i.replace(".", "") for i in csvFileArray[42]]))
arra43 = list(map(int, [i.replace(".", "") for i in csvFileArray[43]]))
arra44 = list(map(int, [i.replace(".", "") for i in csvFileArray[44]]))
arra45 = list(map(int, [i.replace(".", "") for i in csvFileArray[45]]))
arra46 = list(map(int, [i.replace(".", "") for i in csvFileArray[46]]))
arra47 = list(map(int, [i.replace(".", "") for i in csvFileArray[47]]))
arra48 = list(map(int, [i.replace(".", "") for i in csvFileArray[48]]))
arra49 = list(map(int, [i.replace(".", "") for i in csvFileArray[49]]))
arra50 = list(map(int, [i.replace(".", "") for i in csvFileArray[50]]))
arra51 = list(map(int, [i.replace(".", "") for i in csvFileArray[51]]))
arra52 = list(map(int, [i.replace(".", "") for i in csvFileArray[52]]))
arra53 = list(map(int, [i.replace(".", "") for i in csvFileArray[53]]))
arra54 = list(map(int, [i.replace(".", "") for i in csvFileArray[54]]))
arra55 = list(map(int, [i.replace(".", "") for i in csvFileArray[55]]))
arra56 = list(map(int, [i.replace(".", "") for i in csvFileArray[56]]))
arra57 = list(map(int, [i.replace(".", "") for i in csvFileArray[57]]))
arra58 = list(map(int, [i.replace(".", "") for i in csvFileArray[58]]))
arra59 = list(map(int, [i.replace(".", "") for i in csvFileArray[59]]))
arra60 = list(map(int, [i.replace(".", "") for i in csvFileArray[60]]))
arra61 = list(map(int, [i.replace(".", "") for i in csvFileArray[61]]))
arra62 = list(map(int, [i.replace(".", "") for i in csvFileArray[62]]))
arra63 = list(map(int, [i.replace(".", "") for i in csvFileArray[63]]))
arra64 = list(map(int, [i.replace(".", "") for i in csvFileArray[64]]))
arra65 = list(map(int, [i.replace(".", "") for i in csvFileArray[65]]))
arra66 = list(map(int, [i.replace(".", "") for i in csvFileArray[66]]))
arra67 = list(map(int, [i.replace(".", "") for i in csvFileArray[67]]))
arra68 = list(map(int, [i.replace(".", "") for i in csvFileArray[68]]))
arra69 = list(map(int, [i.replace(".", "") for i in csvFileArray[69]]))
arra70 = list(map(int, [i.replace(".", "") for i in csvFileArray[70]]))
arra71 = list(map(int, [i.replace(".", "") for i in csvFileArray[71]]))
arra72 = list(map(int, [i.replace(".", "") for i in csvFileArray[72]]))
arra73 = list(map(int, [i.replace(".", "") for i in csvFileArray[73]]))
arra74 = list(map(int, [i.replace(".", "") for i in csvFileArray[74]]))
arra75 = list(map(int, [i.replace(".", "") for i in csvFileArray[75]]))
arra76 = list(map(int, [i.replace(".", "") for i in csvFileArray[76]]))
arra77 = list(map(int, [i.replace(".", "") for i in csvFileArray[77]]))
arra78 = list(map(int, [i.replace(".", "") for i in csvFileArray[78]]))
arra79 = list(map(int, [i.replace(".", "") for i in csvFileArray[79]]))
arra80 = list(map(int, [i.replace(".", "") for i in csvFileArray[80]]))
arra81 = list(map(int, [i.replace(".", "") for i in csvFileArray[81]]))
arra82 = list(map(int, [i.replace(".", "") for i in csvFileArray[82]]))
arra83 = list(map(int, [i.replace(".", "") for i in csvFileArray[83]]))
arra84 = list(map(int, [i.replace(".", "") for i in csvFileArray[84]]))
arra85 = list(map(int, [i.replace(".", "") for i in csvFileArray[85]]))
arra86 = list(map(int, [i.replace(".", "") for i in csvFileArray[86]]))
arra87 = list(map(int, [i.replace(".", "") for i in csvFileArray[87]]))
arra88 = list(map(int, [i.replace(".", "") for i in csvFileArray[88]]))
arra89 = list(map(int, [i.replace(".", "") for i in csvFileArray[89]]))
arra90 = list(map(int, [i.replace(".", "") for i in csvFileArray[90]]))
arra91 = list(map(int, [i.replace(".", "") for i in csvFileArray[91]]))
arra92 = list(map(int, [i.replace(".", "") for i in csvFileArray[92]]))
arra93 = list(map(int, [i.replace(".", "") for i in csvFileArray[93]]))
arra94 = list(map(int, [i.replace(".", "") for i in csvFileArray[94]]))
arra95 = list(map(int, [i.replace(".", "") for i in csvFileArray[95]]))
arra96 = list(map(int, [i.replace(".", "") for i in csvFileArray[96]]))
arra97 = list(map(int, [i.replace(".", "") for i in csvFileArray[97]]))
arra98 = list(map(int, [i.replace(".", "") for i in csvFileArray[98]]))
arra99 = list(map(int, [i.replace(".", "") for i in csvFileArray[99]]))
arra100 = list(map(int, [i.replace(".", "") for i in csvFileArray[100]]))
arra101 = list(map(int, [i.replace(".", "") for i in csvFileArray[11]]))
arra102 = list(map(int, [i.replace(".", "") for i in csvFileArray[102]]))
arra103 = list(map(int, [i.replace(".", "") for i in csvFileArray[103]]))
arra104 = list(map(int, [i.replace(".", "") for i in csvFileArray[104]]))
arra105 = list(map(int, [i.replace(".", "") for i in csvFileArray[105]]))
arra106 = list(map(int, [i.replace(".", "") for i in csvFileArray[106]]))
arra107 = list(map(int, [i.replace(".", "") for i in csvFileArray[107]]))
arra108 = list(map(int, [i.replace(".", "") for i in csvFileArray[108]]))
arra109 = list(map(int, [i.replace(".", "") for i in csvFileArray[109]]))
arra110 = list(map(int, [i.replace(".", "") for i in csvFileArray[110]]))
arra111 = list(map(int, [i.replace(".", "") for i in csvFileArray[111]]))
arra112 = list(map(int, [i.replace(".", "") for i in csvFileArray[112]]))
arra113 = list(map(int, [i.replace(".", "") for i in csvFileArray[113]]))
arra114 = list(map(int, [i.replace(".", "") for i in csvFileArray[114]]))
arra115 = list(map(int, [i.replace(".", "") for i in csvFileArray[115]]))
arra116 = list(map(int, [i.replace(".", "") for i in csvFileArray[116]]))
arra117 = list(map(int, [i.replace(".", "") for i in csvFileArray[117]]))
arra118 = list(map(int, [i.replace(".", "") for i in csvFileArray[118]]))
arra119 = list(map(int, [i.replace(".", "") for i in csvFileArray[119]]))
arra120 = list(map(int, [i.replace(".", "") for i in csvFileArray[120]]))
arra121 = list(map(int, [i.replace(".", "") for i in csvFileArray[121]]))
arra122 = list(map(int, [i.replace(".", "") for i in csvFileArray[122]]))
arra123 = list(map(int, [i.replace(".", "") for i in csvFileArray[123]]))
arra124 = list(map(int, [i.replace(".", "") for i in csvFileArray[124]]))
arra125 = list(map(int, [i.replace(".", "") for i in csvFileArray[125]]))
arra126 = list(map(int, [i.replace(".", "") for i in csvFileArray[126]]))
arra127 = list(map(int, [i.replace(".", "") for i in csvFileArray[127]]))
arra128 = list(map(int, [i.replace(".", "") for i in csvFileArray[128]]))
arra129 = list(map(int, [i.replace(".", "") for i in csvFileArray[129]]))
arra130 = list(map(int, [i.replace(".", "") for i in csvFileArray[130]]))
arra131 = list(map(int, [i.replace(".", "") for i in csvFileArray[131]]))
arra132 = list(map(int, [i.replace(".", "") for i in csvFileArray[132]]))
arra133 = list(map(int, [i.replace(".", "") for i in csvFileArray[133]]))
arra134 = list(map(int, [i.replace(".", "") for i in csvFileArray[134]]))
arra135 = list(map(int, [i.replace(".", "") for i in csvFileArray[135]]))
arra136 = list(map(int, [i.replace(".", "") for i in csvFileArray[136]]))
arra137 = list(map(int, [i.replace(".", "") for i in csvFileArray[137]]))
arra138 = list(map(int, [i.replace(".", "") for i in csvFileArray[18]]))
arra139 = list(map(int, [i.replace(".", "") for i in csvFileArray[139]]))
arra140 = list(map(int, [i.replace(".", "") for i in csvFileArray[140]]))
arra141 = list(map(int, [i.replace(".", "") for i in csvFileArray[141]]))
arra142 = list(map(int, [i.replace(".", "") for i in csvFileArray[142]]))
arra143 = list(map(int, [i.replace(".", "") for i in csvFileArray[143]]))
arra144 = list(map(int, [i.replace(".", "") for i in csvFileArray[144]]))
arra145 = list(map(int, [i.replace(".", "") for i in csvFileArray[145]]))
arra146 = list(map(int, [i.replace(".", "") for i in csvFileArray[145]]))
arra147 = list(map(int, [i.replace(".", "") for i in csvFileArray[146]]))
arra148 = list(map(int, [i.replace(".", "") for i in csvFileArray[147]]))
arra149 = list(map(int, [i.replace(".", "") for i in csvFileArray[148]]))
arra150 = list(map(int, [i.replace(".", "") for i in csvFileArray[149]]))
arra151 = list(map(int, [i.replace(".", "") for i in csvFileArray[150]]))
arra152 = list(map(int, [i.replace(".", "") for i in csvFileArray[151]]))
arra153 = list(map(int, [i.replace(".", "") for i in csvFileArray[152]]))
arra154 = list(map(int, [i.replace(".", "") for i in csvFileArray[153]]))
arra155 = list(map(int, [i.replace(".", "") for i in csvFileArray[154]]))
arra156 = list(map(int, [i.replace(".", "") for i in csvFileArray[155]]))
arra157 = list(map(int, [i.replace(".", "") for i in csvFileArray[156]]))
arra158 = list(map(int, [i.replace(".", "") for i in csvFileArray[157]]))
arra159 = list(map(int, [i.replace(".", "") for i in csvFileArray[158]]))
arra160 = list(map(int, [i.replace(".", "") for i in csvFileArray[159]]))

print(arra1)

# _______________________________________________________Support Vector Machine Training__________________________________________________________________
from sklearn import svm
from sklearn import metrics

#Input Data
target = [860, 286, 0.33411033, 97347542]

file_ = pd.read_csv("Dataset\SMV\Features_raw.csv", sep=',')
A = np.array(file_[["maximo", "minimo", "media"]])
# Load the training dataSet with Characteristics Maximun, Minimun, Mean, Variance

X = [arra1, arra2, arra3, arra4, arra5, arra6, arra7, arra8, arra9, arra10, arra11, arra12, arra13, arra14, arra15,
     arra16,
     arra17, arra18, arra19, arra20, arra21, arra22, arra23, arra24, arra25, arra26, arra27, arra28, arra29, arra30,
     arra31, arra32, arra33, arra34, arra35, arra36, arra37, arra38, arra39, arra40, arra41, arra42, arra43, arra44,
     arra45,
     arra46, arra47, arra48, arra49, arra50, arra51, arra52, arra53, arra54, arra55, arra56, arra57, arra58, arra59,
     arra60, arra61, arra62, arra63, arra64, arra65, arra66, arra67, arra68, arra69, arra70, arra71, arra72, arra73,
     arra74, arra75,
     arra76, arra77, arra78, arra79, arra80, arra81, arra82, arra83, arra84, arra85, arra86, arra87, arra88, arra89,
     arra90,
     arra91, arra92, arra93, arra94, arra95, arra96, arra97, arra98, arra99, arra100, arra101, arra102, arra103,
     arra104,
     arra105, arra106, arra107, arra108, arra109, arra110, arra111, arra112, arra113, arra114, arra115, arra116,
     arra117,
     arra118, arra119, arra120, arra121, arra122, arra123, arra124, arra125, arra126, arra127, arra128, arra129,
     arra130,
     arra131, arra132, arra133, arra134, arra135, arra136, arra137, arra138, arra139, arra140, arra141, arra142,
     arra143, arra144,
     arra145, arra146, arra147, arra148, arra149, arra150, arra151, arra152, arra153, arra154, arra155, arra56, arra157,
     arra158,
     arra159, arra160]


#Load the categories for the SVM
categories = "Dataset\SMV\Categories.txt"
lista = [line.rstrip('\n') for line in open(categories)]
categorias = [int(x) for x in lista]  # String to Int


y = categorias  # Category:  0 - Seizure , 1 - Walk, 2 - Running
# Load the SVM kernel , type Linear SVC
clf = svm.SVC()
# Learning of the SVM
clf.fit(X, y)
# Prediction of the target
res = clf.predict(target)

if res == 0:
    print("SE DETECTO CONVULSION")
if res == 1:
    print("SE DETECTO CAMINANDO")
if res == 2:
    print("SE DETECTO CORRIENDO")


# from sklearn import svm
# X = [[0, 1, 2], [4,5,6 ], [9,10,23]]
# y = [0, 1, 3]
# clf = svm.SVC()
# clf.fit(X, y)
# res = clf.predict([[90,45,67]])
#
# print(res)