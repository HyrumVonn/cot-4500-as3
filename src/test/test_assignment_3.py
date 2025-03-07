#Euler Method
#func t-y^2
#range 0 < t < 2
#iterations 10
#initial point: f(0) = 1

#Runge-Kutta
#same params

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

    print(y)
    print(x)

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

    print(y)
    print(x)

    return y[iterations]

#Euler(0, 2, 10, 1)
# Euler(0,2,10,.5)

RungeKutta(0,2,10,1)
