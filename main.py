import matplotlib.pyplot as plt
from DataPreprocessing import preprocessing
from PolynomialRegression import getModel
from ListOfRange import getRange

#Grado del polinimio al que se desea ajustar los datos
grado = 3

#Valor minimo y maximo de la variable de entrada
min = 12.2
max = 18.57

#Rango de ajuste
max_range = max - min

#Valores de entrada
x = [12.2,15.33,17.31,18.57]
#Valores de salida
y = [656.3,486.1,434.1,410.2]

#Modelo principal
model = getModel(x,y,grado)

#Valores maximos
x = [12.3,15.37,17.34,18.62]

#Modelo maximo
model_max = getModel(x,y,grado)

#Valores minimos
x = [12.1,15.29,17.28,18.52]

#Modelo minimo
model_min = getModel(x,y,grado)


#Graficacion
x = getRange(max_range,min)
xp = preprocessing(x,grado)
y = model.predict(xp)
y_max = model_max.predict(xp)
y_min = model_min.predict(xp)
plt.plot(x,y)
plt.plot(x,y_max)
plt.plot(x,y_min)

plt.show()

for i,v in enumerate(x):
    exit(-50) if y[i][0] < y_min[i][0] or y[i][0] > y_max[i][0] else None
    print(f'(x: {v}; λ: {round(y[i][0],2)}nm; Min: {round(y_min[i][0],2)}; Max: {round(y_max[i][0],2)})')
