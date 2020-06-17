import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn import linear_model
import pandas

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#prédiction des emissions CO2 d'un véhicule ayant un poid de 2000kg et un volume de 
predicted_co2 = regre.predict([[2000, 1000]])