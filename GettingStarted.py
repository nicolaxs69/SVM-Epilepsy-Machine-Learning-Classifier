# -------------------------------Coeficientes de Fourier------------------------------
import matplotlib.pyplot as plt
from scipy.fftpack import fft, rfft, irfft

list = [line.rstrip('\n') for line in open('Conv_S-1_#3.txt')]
data = [int(x) for x in list] # String to Int

fft(data)

yr = rfft(data)
#print (irfft(yr))
print (fft(data))


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Plot title")
ax1.set_xlabel('Numero de muestras')
ax1.set_ylabel('Muestras Sensor')
ax1.plot(fft(data), c='b', label='Coeficientes de Fourier')
leg = ax1.legend()
plt.show()

# -------------------------------Caracteristicas Estadisticas------------------------------
# from scipy import stats
# from scipy.stats import norm
# import matplotlib.pyplot as plt
# import numpy as np
#
# file = 'Conv_s-1_#3.txt'
# list = [line.rstrip('\n') for line in open(file)]
# data = [int(x) for x in list] # Parsear de String a int
#
#
# # Metodos de la Libreria Statics (scpy.stats), https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
# maximo = np.max(data)
# minimo = np.min(data)
# media  = np.mean(data)
# varianza = np.var(data)
#
# a = "Maximo:",maximo
# b = "Minimo:",minimo
# c = "Media:", media
# d = "Varianza:",varianza
#
# print ("Maximo:",maximo)
# print ("Minimo:",minimo)
# print ("Media:", media)
# print("Varianza:",varianza)
#
#
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
#
# ax1.set_title(file)
# ax1.set_xlabel('Numero de muestras')
# ax1.set_ylabel('Muestras Sensor')
# ax1.plot(data, c='b', label=a+b+c+d)
#
# leg = ax1.legend()
#
# plt.show()

# ------------------------------- Preprocesamiento------------------------------
# This is anothe way to extract features, not used but it is considered interesting and useful in any just in case

# from sklearn import preprocessing
# import numpy as np
#
# file = 'Caminando_Suj-2_#1.txt'
# list = [line.rstrip('\n') for line in open(file)]
# data = [int(x) for x in list] # Parsear de String a int
#
#*****Reshape your data either X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.

# data_fit = np.array(data).reshape((len(data), -1))
# #print(data_fit)

# # The scaled data have a mean of zero and unit variance
# data_scaled = preprocessing.scale(data)

# print('Media Cero:',data_scaled.mean(axis=0))
# print('Varianza Unitaria:',data_scaled.std(axis=0))


#*****API to calculate mean and standard deviation

# scaler = preprocessing.StandardScaler().fit(data)
# print('Media Scalar API:',scaler.mean_)
# print('Scala API:', scaler.scale_)
# #print('Transform API:', scaler.transform(data))
#
# _________________________________________________________SVM Classifier________________________________________________
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
# import csv
#
# # Datasets:
#
# # Seizure:
seizure_1= "Dataset\Convulsion\Conv_s-1_#1.txt"
seizure_2= "Dataset\Convulsion\Conv_s-1_#2.txt"
seizure_3= "Dataset\Convulsion\Convulsion_Test.txt"
#
lista = [line.rstrip('\n') for line in open(seizure_3)]
data = [int(x) for x in lista]  # String to Int

#print(data)
#
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

data = array3
maximo = np.max(data)
minimo = np.min(data)
media  = np.mean(data)
varianza = np.var(data)
#
# a = "Maximo:",maximo
# b = "Minimo:",minimo
# c = "Media:", media
# d = "Varianza:",varianza
#
# print ("Maximo:",maximo)
# print ("Minimo:",minimo)
# print ("Media:", media)
# print("Varianza:",varianza)

