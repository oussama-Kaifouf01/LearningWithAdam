#Verfie si x est divisible par 5

x = input("Entrez un nombre: ") #input c'est une fonction qui sert à demander à l'utilisateur d'entrer une valeur et la stoquer dans une variable


if (x%5==0):
    print(x,"est divisible par 5")
if (x%5!=0):
    print(x,"n'est pas divisible par 5")