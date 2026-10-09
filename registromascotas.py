import os
nombre_mascotas=[""]*3 
edad_mascotas=[0]*3
def Insertar():
     for i in range(len(nombre_mascotas)): #.Length en c#
        nombre_mascotas[i]=input(f"Ingrese nombre de la mascota: ")
        edad_mascotas[i]=int(input(f"Ingrese edad de la mascota: "))
def Mostrar():
    for i in range(len(nombre_mascotas)): #.Length en c#
        print(f"Nombre de mascota: {nombre_mascotas[i]}, edad: {edad_mascotas[i]}")

def main():
    global nombre_mascotas, edad_mascotas
    #arreglos paralelos ambas listas deben tener la misma longitud=3
    nombre_mascotas=[""]*3 #iniciar la lista vacia para cadenas
    edad_mascotas=[0]*3 #iniciar la lista vacia para numeros enteros de longitud 3
    opcion=0
    while opcion != 4:
        os.system('cls' if os.name=='nt' else 'clear') #limpiar la pantalla
        print("[1] Insertar mascotas (nombre | edad)")
        print("[2] Mostrar mascotas (nombre | edad)")
        print("[3] Eliminar mascotas")
        print("[4] Salir")
        opcion=int(input(" -Seleccione una opcion: "))
        if opcion==1:
            Insertar()
        elif opcion==2:
            Mostrar()
        elif opcion==3:
            print("")
        elif opcion==4:
            print("SALIENDO.....")
        else: print("Opcion invalida")
        if opcion!=4: input("presione para continuar..")#espere a la interaccion del usuario para recargar el menu
main()