print("-----------------CONSOLE GAME CORPORATION-----------------")

print("Consolas disponibles")

print("0. x box 360")
print("1. play station 3")
print("2. wii")
print("3. genkiuo")

codigo = int(input("Selecciona la consola por codigo: "))

while codigo > 3:
    print("NO EXISTE ESE CODIGO DE CONSOLA")
    print("POR FAVOR, INGRESE DE NUEVO EL CODIGO")
    break
    
if codigo == 0 :
    print("Ha seleccionado el x box 360 ")
elif codigo == 1:
    print("Ha seleccionado la play station 3")
elif codigo == 2:
    print("Ha seleccionado la wii")    
elif codigo == 3:
    print("Ha seleccionado la genkiou")
    
print("Ingrese sus datos personales para iniciar el tramite")
nombre = input("NOMBRE COMPLETO: ")
apellido = input("APELLIDOS COMPLETOS: ")
edad = int(input("EDAD: "))
celular = int(input("N° CELULAR: "))
dni = int(input("DNI: "))
distrito = input("DISTRITO: ")

print("DATOS REGISTRADOS EXITOSAMENTE")

diccionario = {
    "NOMBRE" : nombre,
    "APELLIDO" : apellido,
    "EDAD" : edad,
    "CELULAR" : celular,
    "DNI" : dni,
    "DISTRITO" : distrito
}

print(diccionario)