import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#REGRESSION POLYNOMIALE

x_poly = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y_poly = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x_poly, y_poly, 3))

myline = numpy.linspace(1, 22, 100)

#prédiction d'une voiture passant à 20h
speed = mymodel(20)

plt.scatter(x_poly, y_poly)
plt.plot(myline, mymodel(myline))
plt.show()
#print(r2_score(y_poly, mymodel(x_poly)))
print(speed)