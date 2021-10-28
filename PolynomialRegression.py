from sklearn.linear_model import LinearRegression
from DataPreprocessing import preprocessing,getArray

def getModel(x,y,grado):
    #Lista de datos de variable de entrada
    x = preprocessing(x,grado)
    #Lista de datos de variable de salida
    y = getArray(y)

    #Entrenamiento y ajuste del modelo
    model = LinearRegression()
    model.fit(x,y)
    return model
