#Euler Method
#func t-y^2
#range 0 < t < 2
#iterations 10
#initial point: f(0) = 1

#Runge-Kutta
#same params

def f(t, y):
    return t - y * y

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
    
    stepsize = (rangeUpper - rangeLower) / iterations



Euler(0, 2, 10, 1)
