# 5- Question Bonus : Implémentation de la formule Pricer :

def d1(S, X, T, r, sigma):
    return(log(S / X) + (r + sigma**2 /2.) * T) / (sigma * sqrt(T))

def d2(S, X, T, r, sigma):
    return d1(S, X, T, r, sigma) - sigma * sqrt(T)

def call(S, X, T, r, sigma):
    return S * norm.cdf(d1(S, X, T, r, sigma)) - X * exp(-r * T) * norm.cdf(d2(S, X, T, r, sigma))
  
def put(S, X, T, r, sigma):
    return X * exp(-r * T) - S + call(S, X, T, r, sigma)