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

    #print(y)
    #print(x)


Euler(0, 2, 10, 1)
# Euler(0,2,10,.5)
