import numpy
from scipy import stats
import matplotlib.pyplot as plt

#REGRESSION LINEAIRE

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

x2 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y2 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

xmoyenne = numpy.mean(speed)
xmedian = numpy.median(speed)
xmode = stats.mode(speed)
xecart_type = numpy.std(speed)
xvariance = numpy.var(speed)
xpercentiles = numpy.percentile(speed, 60)

slope, intercept, r, p, std_err = stats.linregress(x2, y2)

def myfunc(x2):
    return slope * x2 + intercept

mymodel = list(map(myfunc, x2))

predict_speed = myfunc(20)

#print(xpercentiles)

plt.scatter(x2, y2)
plt.plot(x2, mymodel)
plt.show()
print(predict_speed)