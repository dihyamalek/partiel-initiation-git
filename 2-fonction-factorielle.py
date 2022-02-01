# 2- implementation de la fonction factorielle

def factorielle(n):
    return factorielle(n - 1) * n if n > 1 else 1

factorielle(5)