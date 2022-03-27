	Purpose:  This program will find the value of the european call option and put option on the underlyting assest S that 
               follows a geometric brownian motion through the fourier series by using Fast Fourier Transform.
	            
	Algorithm: Using Fast fourier transform to find the European call option or put option based on the 
                 dumping parameters(alpha value) as positive or negative.Positive value of alpha implies the European call
                 option and negative value of alpha denotes the European put option.
                
	
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
                
    Analytical Solutions:
            Positive  and Negative value of damping parameters respectively give the 
            Values of European Call option and Put option. Their role is not significant,
            but plugging the very small and big dammping parameters affect the result very
            significantly. In our problem, we are getting the same outputs although damping 
            parametrs are different.
                     
                     
