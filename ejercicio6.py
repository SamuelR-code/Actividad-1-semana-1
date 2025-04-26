#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.
numero_secreto= 7
numero_del_participante = int(input("Adivine el numero secreto")) 

if numero_del_participante > numero_secreto:
 print("el numero es mayor")
elif numero_del_participante < numero_secreto:
 print("el numero es menor")
else: 
    print("ganaste")