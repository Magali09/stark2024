from data_stark import lista_personajes



def limpiar_pantalla():
    import os
    os.system("cls")# PARA LIMPIAR PANTALLA
    return input("Presione la tecla enter para continuar: ")

#I. Ordenar el código implementando una función para cada uno de los valores informados.
def menu()->str:
    limpiar_pantalla()
    print(f"{'Menu de opciones':^100s}")#:^100s imprime msj de 10 caracteres y menu de opciones queda centrado en el
    print("1- Imprimir el nombre de cada superhéroe: ")
    print("2- Imprimir nombre y altura: ")
    print("3- Imprimir super heroe más alto: ")
    print("4- Imprimir super heroe menos alto: ")
    print("5- Imprimir el promedio de las alturas: ")
    print("6- Imprimir el nombre del mas alto y menos alto: ")
    print("7- Imprimir el calculo del mas y menos pesado: ")
    print("8- Salir ")
    
    return input("Ingrese una opcion: ")
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def imprimir_nombres(lista_personajes):
    for personaje in lista_personajes:
        print(personaje["nombre"])
        


# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def imprimir_nombre_altura(lista_personajes):
    for personaje in lista_personajes:
        print(f"El nombre del personaje es: {personaje['nombre']} y su altura: {personaje['altura']}")
        


#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def imprimir_mas_alto(lista_personajes):
    flag_mas_alto = True
    maxima_altura = 0
    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if flag_mas_alto or altura > maxima_altura:
            maxima_altura = altura
            nombre_mas_alto = personaje["nombre"]
            flag_mas_alto = False
            mensaje = (f"El super heroe mas alto es: {maxima_altura} y se llama: {nombre_mas_alto}")
    return mensaje





#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

def imprimir_mas_bajo(lista_personajes):
    flag_mas_bajo = True
    minima_altura = 0
    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if flag_mas_bajo or altura < minima_altura:
            minima_altura = altura
            nombre_mas_bajo = personaje["nombre"]
            flag_mas_bajo = False
            mensaje = (f"El super heroe menos alto es: {minima_altura} y se llama: {nombre_mas_bajo}")
    return mensaje



#F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)

def imprimir_promedios_personajes(lista_personajes):
    acumulador_altura = 0
    contador_altura = 0
    for personaje in lista_personajes:
        acumulador_altura += float(personaje["altura"])
        contador_altura += 1
    promedio_altura = acumulador_altura / contador_altura
    return (f"El promedio de las alturas es: {promedio_altura}")



#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
#H. Calcular e informar cual es el superhéroe más y menos pesado.
def imprimir_pesos_personajes(lista_personajes):
    bandera_mas_pesado = True
    bandera_menos_pesado = True
    mas_pesado = 0
    menos_pesado = 0
    for personajes in lista_personajes:
        peso = float(personajes["peso"])
        if peso > mas_pesado or bandera_mas_pesado == True:
            mas_pesado = float(personajes["peso"])
            nombre_mas_pesado = personajes["nombre"]
            bandera_mas_pesado = False
        if peso < menos_pesado or bandera_menos_pesado == True:
            menos_pesado = float(personajes["peso"])
            nombre_menos_peso = personajes["nombre"]
            bandera_menos_pesado = False
            mensaje = (f"El personaje mas pesado es:{mas_pesado} y  se llama: {nombre_mas_pesado}.\
            El personaje menos pesado es: {menos_pesado} y se llama: {nombre_menos_peso}")
    return mensaje

print(imprimir_pesos_personajes(lista_personajes))

def pausar():
    import os
    os.system("pause")

def pedir_confirmacion(mensaje:str)->bool:
    respuesta = input(mensaje).lower()
    return respuesta == "si"