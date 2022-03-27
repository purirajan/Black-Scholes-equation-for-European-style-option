Purpose:  This program will find the value of the european call option and put option on the underlyting assest S that 
               follows a geometric brownian motion through the fourier series by using the trapezoidal rule.
	            
	Algorithm: Trapezoidal Rule
                Fourier Series
	
	Arguments: S - Price of underlying asset at time t = 0.
	           K - Strike price
	           T - Maturity date, measured in fraction (or a multiple) of a year. T > 0
	           sigma - Standard deviation of log (S)
	           r - interest rate
	Usage:	   
                S0 = 100 # initial stock price
                K = 80  # strike price
                T = 1.0 # maturity time
                sigma = 0.50 # volatility
                r = 0.05 # interest rate    
                     
	---------------------------------------------------------------------------------------------"""
import numpy as np
from TrapezoidalRule import*
def main():
    S0= 100.00
    K =80
    k = np.log(K)
    r = 0.05
    T = 1.0
    t0 = 0
    sigma = 0.50
    B =50
    N =1000
    h = float(B)/N
    alpha= np.array([2.5,5,10,-2.5,-5,-10])
    L= len(alpha)
    x0 = np.log(S0)
    Sum = Trapezoidal(lambda w: np.exp(1j * w * k - r*(T - t0) - 1j * 
    (x0 + (r - sigma ** 2 / 2) * T) * (w + (alpha+ 1) * 1j) - 
    sigma ** 2 / 2 * T * (w + (alpha+ 1) * 1j) ** 2) / 
    ((alpha- 1j * w) * (alpha - 1j * w +1)),0,B,N).real
    Final_Sum = np.exp(-alpha * k) / np.pi * Sum
    Full_Sum = Trapezoidal(lambda w: np.exp(1j * w * k - r*(T - t0) - 1j * 
    (x0 + (r - sigma ** 2 / 2) * T) * (w + (alpha+ 1) * 1j) - 
    sigma ** 2 / 2 * T * (w + (alpha+ 1) * 1j) ** 2) / 
    ((alpha- 1j * w) * (alpha - 1j * w +1)),-B,B,N).real
    Full_Final_Sum = np.exp(-alpha * k) / (2* np.pi) * Full_Sum
    print ('\n Price of European call and put options \n')

    print ('Parameters:\n')
    print ('     S0=%g, K=%g, T=%g, r=%g, sigma=%g, B=%g, N=%g' % (S0, K, T, r, sigma, B, N))
    print('\n Half-frequency Domain[0,B]')
    print ('\n%15s   %12s ' %('Alpha Value', 'Eur Call Price(+ve)/Put Price(-ve)'))
    for i in range(L):
        print ('%12.1f %22.4f' % (alpha[i],Final_Sum[i]))
    print('\n Full-frequency Domain[-B,B]')
    print ('\n%15s   %12s ' %('Alpha Value', 'Eur Call Price(+ve)/Put Price(-ve)'))
    for i in range(L):
        print ('%12.1f %22.4f' % (alpha[i],Full_Final_Sum[i]))   
main()
