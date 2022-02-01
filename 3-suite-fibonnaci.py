# 3- implementation de la suite de Fibonnaci

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
        
def fibonacci_suite(n):
    for i in range(n):
        print(fibonacci(i), end=", ")

nterms = int(input("Entrez un nombre: "))
fibonacci_suite(nterms)