#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

numero_1 = int(input("dime el primer numero"))
numero_2 = int(input("dime el segundo numero"))

if numero_1>numero_2:
   print("El primer numero es mayor")
elif numero_1<numero_2:
   print("El segundo numero es mayor ")
else: 
   print("Los numeros son iguales")
