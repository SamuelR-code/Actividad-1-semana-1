#Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".

contraseña = "python123"

contraseña_input=input("ingrese la contraseña-")

if contraseña_input == contraseña:
  print("Acceso concedido")
else: 
  print("Acceso denegado")