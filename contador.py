print("---------------REGISTRO DE NOTAS---------------")

print("------------INDICACIONES-----------")
print(" SI TU PROMEDIO FINAL PASA DE LOS 50 OBTIENES CERTIFICADO")

cantidad = 0

tarea = int(input("Ingrese la cantidad de tareas que va a presentar: "))

for i in range(tarea):
    
    
    nota = int(input(f"CALIFICACION DEL TRABAJO {i}: "))
    
    cantidad = cantidad + nota
    while nota > 20:
        print("ERROR!!!!")
        nota = int(input(f"CALIFICACION DEL TRABAJO {i}: "))

print("DATOS REGISTRADOS CORRECTAMENTE ....................")

print(f"la suma de sus notas es de {cantidad}")

print("SACANDO EL PROMEDIO")

prom = cantidad / 5 

print(prom)

if prom >= 10:
    print("FELICIDADES, OBTUVO SU CERTIFICADO")
    
else :
    print("NO ALCANZO EL PUNTAJE PARA OBTENER EL CERTIFICADO")

