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
    return 1.25

rangeU = 2
rangeL = 0
iterations = 10
initialPoint = 1

print(Euler(rangeL, rangeU, iterations, initialPoint))

print()

print(RungeKutta(rangeL, rangeU, iterations, initialPoint))
