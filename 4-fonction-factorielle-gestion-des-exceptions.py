# 4 - Création de fonction comportant des modules de gestions des exceptions (5 points) :
# - Saisie d'une chaine de caractère dans les arguments de la fonction
# - Saisie un nombre complexe
# - Saisie d'un nombre négatif
# - Saisie d'un très grand nombre
# - Saisie d'un très petit nombre

def factorielle_(n):
    if (isinstance(n, str) or isinstance(n, float) or n < 0 or n > 999):
        print("Erreur: Vous devaiez saisir un nombre entier positif inferieur à 1000.")
        return
    
    return factorielle(n - 1) * n if n > 1 else 1

factorielle_("5")
factorielle_(5.5)
factorielle_(-2)
factorielle_(1000)