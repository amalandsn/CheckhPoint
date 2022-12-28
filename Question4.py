# Question 4
s = input("donner un mot :")
n = input("donner le chiffre à retirer")
n = int(n)
def missing_char(s, n):
    # valeur de retour : le mot avec l'index n supprimé
    return s[:n] + s[n+1:]
   #  print(s[:n] + s[n+1:])

print(missing_char(s, n))  
