#Hyrum VonNiederhausern

def f(t, y):
    return t - y * y

# #example from slides
# def f(t, y):
#     return y - t * t + 1

def Euler(rangeLower, rangeUpper, iterations, initailPoint):
    if(rangeLower > rangeUpper):
        temp = rangeUpper
        rangeUpper = rangeLower
        rangeLower = temp
    
    if(rangeLower == rangeUpper):
        print(f"Error, range must have non-equal start and end points (current {rangeLower} and {rangeUpper})")
        return
    
    if(iterations <= 0):
        print(f"Error, Iterations must be positive. Currently {iterations}")
        return
    
    y = []
    x = []
    #x.append(rangeLower)
    stepsize = (rangeUpper - rangeLower) / iterations

    for i in range(iterations + 1):
        x.append(rangeLower + stepsize * i)
        
        if(i == 0):
            y.append(initailPoint)
            continue

        y.append(y[i - 1] + stepsize * f(x[i-1], y[i-1])) 

    return y[iterations]


def RungeKutta(rangeLower, rangeUpper, iterations, initailPoint):
    if(rangeLower > rangeUpper):
        temp = rangeUpper
        rangeUpper = rangeLower
        rangeLower = temp
    
    if(rangeLower == rangeUpper):
        print(f"Error, range must have non-equal start and end points (current {rangeLower} and {rangeUpper})")
        return
    
    if(iterations <= 0):
        print(f"Error, Iterations must be positive. Currently {iterations}")
        return
    
    y = []
    x = []
    #x.append(rangeLower)
    stepsize = (rangeUpper - rangeLower) / iterations
    stepsize2 = stepsize / 2

    for i in range(iterations + 1):
        x.append(rangeLower + stepsize * i)
        
        if(i == 0):
            y.append(initailPoint)
            continue

        k1 = stepsize * f(x[i-1], y[i-1])
        k2 = stepsize * f(x[i-1] + stepsize2, y[i-1] + k1 / 2)
        k3 = stepsize * f(x[i-1] + stepsize2, y[i-1] + k2 / 2)
        k4 = stepsize * f(x[i], y[i-1] + k3)

        y.append(y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6) 

    return y[iterations]

#initialize, both will be using the same values
rangeU = 2
rangeL = 0
iterations = 10
initialPoint = 1

#euler
print(Euler(rangeL, rangeU, iterations, initialPoint))

print()

#RungeKutta
print(RungeKutta(rangeL, rangeU, iterations, initialPoint))

print()
