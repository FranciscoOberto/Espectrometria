from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def preprocessing(x,grado):
    return PolynomialFeatures(grado).fit_transform(getArray(x))

def getArray(x):
    return np.array(x).reshape(-1,1)
