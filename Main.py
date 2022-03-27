	---------------------------------------------------------------------------------------------"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from FourierSeries import*
from FFT import*

def main():
    Alpha1 = [-10,-5,-2.5] ## dumping parameters
    Alpha = [2.5,5,10]
    B = 50.0 
    N = 2**10 
    S0 = 100.0 # initial Stock Price
    x0 = np.log(S0)
    K = 80.0 # Strike Price
    K0 =20
    r = 0.05 # rate of interest
    sig = 0.50 # Volatility
    T = 1.0 # Maturity Date
    h = float(B)/(N-1) 
    k0 =np.log(K0) # mimimum value of K
    delta_k =float( 2*(np.pi)/(h*N))
    V = []
    k_n=[]
    for i in range(N):
        k_n.append(k0 + i*delta_k)
    print ('\n Price of European call and put options \n')

    print ('Parameters:\n\n')
    print ('     S0=%g, K=%g, T=%g, r=%g, sigma=%g, B=%g, N=%g' % (S0, K, T, r, sig, B, N))
    print('\n\n Half-frequency Domain[0,B]')
    print ('\n%15s   %16s ' %('Alpha Value', 'Eur Call Price'))
  ############################################################################  
    for alpha in Alpha:
        V = value(k0, S0, K, r, sig, T, h, alpha,N)
        f = P(k0, S0, K, r, sig, T, h, alpha,N)
        k = A(k0, S0, K, r, sig, T, h, alpha,N)
        print ('%12.1f %16.4f' % (alpha,f(np.log(K))))
    #########################################################################
    for alpha in Alpha:
        
        plt.axis([20,300,-10,100])
        #print(min(k))
        plt.plot(np.exp(k_n),V,'--')
        plt.xlabel(" Kn")
        plt.ylabel(" Vn")
        plt.show()
##############################################################################
    print ('\n%15s   %16s ' %('Alpha Value', 'Eur Put Price'))     
    for alpha in Alpha1:
        V = value(k0, S0, K, r, sig, T, h, alpha,N)
        f = P(k0, S0, K, r, sig, T, h, alpha,N)
        k = A(k0, S0, K, r, sig, T, h, alpha,N)
        print ('%12.1f %16.4f' % (alpha,f(np.log(K))))
 ############################################################################
    for alpha in Alpha1:
        
        plt.axis([20,300,-10,100])
        #print(min(k))
        plt.plot(np.exp(k_n),V,'red')
        plt.plot(np.exp(k_n),value(k0, S0, K, r, sig, T, h, -alpha,N),'green')
        plt.xlabel(" Kn")
        plt.ylabel(" Vn")
        plt.show()
##############################################################################
   
   
   
main()
