#Pide un número al usuario. Di si es positivo, negativo o si es cero.

numero = int(input("ingrese un numero"))
if numero >= 1 :
    print("es un numero positivo")
elif numero == 0:
    print("su numero es cero")
else: print("es un numero negativo")    
