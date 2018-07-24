import numpy as np

from matplotlib import pyplot as plt
def gradient_descent(x,y):
    #staring with slope=0,intercept=0
    theta1=0
    theta0=0
    iterations = 10000
    m = len(x)  #for number of training examples
    learning_rate =0.01  #taking baby step for applying convergence

    for i in range(iterations):
        h = theta0+theta1*x      #h(x)=theta0+theta1*X equation of line
        error = (1/2*m) * sum([values**2 for values in (y-h)])  #squared error
        theta1_der = -(1/m)*sum(x*(y-h))
        theta0_der = -(1/m)*sum(y-h)
        theta1 = theta1 - learning_rate * theta1_der 
        theta0 = theta0 - learning_rate * theta0_der
       
    
    values=[4,5,6,7,8,9]
    for v in values:
        pred=theta0+theta1*v
        print(pred)

        
     

x = np.array([2,4,3,6,8,8,10])
y = np.array([10,9,6,6,6,3,2])

gradient_descent(x,y)