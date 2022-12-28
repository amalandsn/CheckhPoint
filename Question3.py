# Question 3
n = input("Donner un nombre :")  
n = int(n)

result = {}  # Dictionnaire vide où stocker le résultat

for i in range(1, n+1):  # n inclus
    result[i] = i*i  # ajout de la valeur de key au dictionnaire

print(result)  # affichage du dictionnaire