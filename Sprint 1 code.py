# -*- coding: utf-8 -*-

'''
Un-documented code (booo!) for trial documentation-sprint. 
'''

import numpy as np




def quadratic_formula(a,b,c):
        """Calculates the real roots for ax^2+bx+c=0

        :param a: quadratic coefficient
        :type a: float, optional
        :param b: linear coefficient
        :type b: float, optional
        :param c: linear coefficient
        :type c: float, optional
        
        :raises: raises ValueError if the discriminant is less than zero
        :return: List of quadratic polynomial roots
        :rtype: list
        """
        d = b**2-4*a*c # discriminant

        if d < 0:
            raise ValueError("This equation has no real solution")
        elif d == 0:
            x = (-b+np.sqrt(b**2-4*a*c))/2*a
            sol = [x]
            return sol
        else:
            x1 = (-b+np.sqrt(b**2-4*a*c))/2*a
            x2 = (-b-np.sqrt(b**2-4*a*c))/2*a
            sol = [x1, x2]
            return sol


# simple numerical integration of f(x) over an interval x: [x_lower, x_upper] using composite trapezoid rule.

def simple_integrate(f, x):
    """Computes the definite integral of a function from the lower to the upper limit using composite trapezoid rule.

    :param f: function to be integrated.
    :param x:  [x_lower, x_upper] lower limit of integration upper limit of integration
    :raises: raises ValueError if the discriminant is less than zero
    :return: integral value
    :rtype: float
    """
    int_sum = 0

    for i in range(x.size-1):
        int_sum += 0.5*(x[i+1] - x[i])*(f[i] + f[i+1])
    
    return int_sum


# function for nth Fibonacci number 
  
def fibonacci(n): 
    """Computes the nth fibonacci number, starting at 0.

    :param n: the index of the Fibonacci number to be computed
    :raises: raises ValueError if n is less than 1
    :return: nth fibonacci number
    :rtype: int
    """
    if n<=0: 
        raise ValueError("Input cannot be less than 1") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)  



# convert time in seconds to hours, minutes and seconds

def get_hms(t_sec):
    """Converts time in seconds to hours, minutes, and seconds.

    :param t_sec: time in seconds
    :return: time in hours, minutes, and seconds
    :rtype: list
    """

    h = t_sec//3600

    m = (t_sec - h*3600)//60

    s = t_sec%60

    return h,m,s #question: does it return a list? Or maybe not?

