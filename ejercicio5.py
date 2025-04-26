#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.


total=float(input("ingrese el total de su cuenta"))
print("opciones de propina")
print ("(1) 10%")
print("(2) 15%")
print("(3) 20%")
propina_elegida =input("elige una opcion")

if propina_elegida=="1":

    total_con_propina=total*0.10
    print("propina es de ",total_con_propina)
elif propina_elegida=="2":

    total_con_propina=total*0.15
    print("propina es de ",total_con_propina)
elif propina_elegida=="3":

    total_con_propina=total*0.20
    print("propina es de ",total_con_propina) 

else: ("valor incorrecto")


