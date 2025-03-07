#Hyrum VonNiederhausern

def BaseFunction(t, y):
    return t - y * y

def Euler(rangeLower, rangeUpper, iterations, initailPoint):
    return 1.24

def RungeKutta(rangeLower, rangeUpper, iterations, initailPoint):
    return 1.25

rangeU = 2
rangeL = 0
iterations = 10
initialPoint = 1

Euler(rangeL, rangeU, iterations, initialPoint)

RungeKutta(rangeL, rangeU, iterations, initialPoint)
