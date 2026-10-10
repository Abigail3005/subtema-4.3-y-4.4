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
def eliminar(nombreaborrar):
    for i in range(len(nombre_mascotas)):
        #buscar a la mascota que quiero borrar
        if nombre_mascotas[i]==nombreaborrar: #encontre la mascota que quiero borrar
            for j in range(i,len(nombre_mascotas)-1): #penultimo registro
                #desplazando los elementos hacia la izquierda
                nombre_mascotas[j]=nombre_mascotas[j+1]
                edad_mascotas[j]=edad_mascotas[j+1]
                #dejar en blanco la ultima ubicacion
                nombre_mascotas[-1]=""
                edad_mascotas[-1]=0
                print(f"mascota eliminada {nombre_mascotas[i]}")
                return #detener la busqueda de mascotas con el mismo nombre
def ordenar():
    for i in range(len(nombre_mascotas)-1):
        for j in range(len(nombre_mascotas)-1-i):
            if nombre_mascotas[j]>nombre_mascotas[j+1]:
                aux=nombre_mascotas[j]
                nombre_mascotas[j]=nombre_mascotas[j+1]
                nombre_mascotas[j+1]=aux
def main():
    global nombre_mascotas, edad_mascotas
    #arreglos paralelos ambas listas deben tener la misma longitud=3
    nombre_mascotas=[""]*3 #iniciar la lista vacia para cadenas
    edad_mascotas=[0]*3 #iniciar la lista vacia para numeros enteros de longitud 3
    op=0
    while op != 5:
        os.system('cls' if os.name=='nt' else 'clear') #limpiar la pantalla
        print("[1] Insertar mascotas (nombre | edad)")
        print("[2] Mostrar mascotas (nombre | edad)")
        print("[3] Eliminar mascotas")
        print("[4] Ordenar mascotas alfabeticamente")
        print("[5] Salir")
        op=int(input(" -Seleccione una opcion: "))
        if op==1:
            Insertar()
        elif op==2:
            Mostrar()
        elif op==3:
            mascotaaborrar=input(" -Ingrese nombre a borrar: ")
            eliminar(mascotaaborrar)
        elif op==4:
            ordenar()
        elif op==5:
            print("SALIENDO.....")
        else: print("Opcion invalida")
        if op!=5: input("presione para continuar..")#espere a la interaccion del usuario para recargar el menu
main()