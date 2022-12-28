# Question 7
import math  # Module math

C = 50
H = 30

# Taper les valeurs séparées par des virgules
D_str = input("Taper les valeurs D séparées par des virgules: ")

# split de D_str en une liste d'entier
D_values = [int(x) for x in D_str.split(',')]

# calcul et affichage de la valeur de Q pour chaque valeur de D
for D in D_values:
    Q = math.sqrt((2 * C * D) / H)  # calcul de Q
    print(round(Q))  # affichage de l'arrondi de Q