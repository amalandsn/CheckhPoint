# Question 2
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
m = input("entrez un nombre :")
m = int(m)
print (factorial(m))
