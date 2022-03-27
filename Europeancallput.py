import numpy as np
import scipy.stats as ss 

def d1(S, K, r, delta, sigma, T):
    return (np.log(S/K) + (r -delta + sigma**2 / 2) * T)/(sigma * np.sqrt(T))
 
def d2(S, K, r, delta, sigma, T):
    return (d1(S, K, r,delta, sigma, T) - (sigma * np.sqrt(T)))
    
def main():
    
    S= 100.0 # S denotes the stock price.
    K= 100.0 # K denotes the strike price.
    T=1.0 # T denotes the maturity period.
    r= 0.05 # r denotes the rate of interest.
    delta = 0.025 # delta denotes the time continous divident yield.
    sigma = float(input(" Enter the value of sigma in between 0.1 to 1.0 :")) # sigma is volatility.
    # F() is the standard normal cumulative distribution = ss.norm.cdf()
    # vc denotes the European call option at the present time( t=0).
    # vp denotes the European put option at the present time(t=0).
    vc= S * ss.norm.cdf(d1(S, K, r, delta, sigma, T)) * np.exp((-delta) * T) - K * np.exp(-r * T) * ss.norm.cdf(d2(S, K, r,delta, sigma, T))
    vp= -S * ss.norm.cdf(-d1(S, K, r, delta, sigma, T)) * np.exp((-delta) * T) + K * np.exp(-r * T) * ss.norm.cdf(-d2(S, K, r,delta, sigma, T))
    print("The value of  European call option is",vc)
    print("The value of  European put option is",vp)


main()
