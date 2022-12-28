# Question 1
result = []  # Création d'une liste vide

for i in range(2000, 3201):  
    if i % 7 == 0 and i % 5 != 0: 
        result.append(i)  # si ok ajout du nombre dans la liste

print(result)  # affichage du résulta
