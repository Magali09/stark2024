from data_stark import lista_personajes


def limpiar_pantalla():
    import os
    os.system("cls")# PARA LIMPIAR PANTALLA
    return input("Presione la tecla enter para continuar: ")

def menu():
    
    limpiar_pantalla()
    print(f"{'Menu de opciones':^100s}")#:^100s imprime msj de 10 caracteres y menu de opciones queda centrado en el
    print("1.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M: ")
    print("2.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F: ")
    print("3.Recorrer la lista y determinar cuál es el superhéroe más alto de género M : ")
    print("4.Recorrer la lista y determinar cuál es el superhéroe más alto de género F: ")
    print("5.Recorrer la lista y determinar cuál es el superhéroe más bajo de género M: ")
    print("6.Recorrer la lista y determinar cuál es el superhéroe más bajo de género F: ")
    print("7.Recorrer la lista y determinar la altura promedio de los superhéroes de género M: ")
    print("8.Recorrer la lista y determinar la altura promedio de los superhéroes de género F: ")
    print("9.Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 a 6): ")
    print("10.Determinar cuántos superhéroes tienen cada tipo de color de ojos: ")
    print("11.Determinar cuántos superhéroes tienen cada tipo de color de pelos: ")
    print("12.Determinar cuántos superhéroes tienen cada tipo de inteligencia: ")
    print("13.Listar todos los superhéroes agrupados por color de ojos: ")
    print("14.Listar todos los superhéroes agrupados por color de pelo: ")
    print("15.Listar todos los superhéroes agrupados por tipo de inteligencia: ")
    print("16. salir: ")

    
    return input("Ingrese una opcion: ")
    
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

def imprimir_genero_masculino(lista_personajes):
    
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            print(personaje["nombre"])




#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F    
def imprimir_genero_femenino(lista_personajes):
    
     for personaje in lista_personajes:
        if personaje["genero"] == "F":
            print(personaje["nombre"])


    
#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def imprimir_alto_masculino(lista_personajes):
    maximo_altura_masculino = 0
    bandera_mas_alto_masculino = True
    for personajes in lista_personajes:
         if personajes["genero"] == "M":  
            altura = float(personajes["altura"])
            if bandera_mas_alto_masculino == True or altura > maximo_altura_masculino:
                maximo_altura_masculino = float(personajes["altura"])
                nombre_mas_alto_maculino = personajes["nombre"]
                bandera_mas_alto_masculino = False
    print(f"El masculino mas alto es: {nombre_mas_alto_maculino} y su altura es: {maximo_altura_masculino}") 



#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

def imprimir_alto_femenino(lista_personajes):
    maxima_altura_femenino = 0
    bandera_mas_alta_femenina = True
    for personajes in lista_personajes:
        if personajes["genero"] == "F":
            altura = float(personajes["altura"])
            if bandera_mas_alta_femenina == True or altura > maxima_altura_femenino:
                maxima_altura_femenino = float(personajes["altura"])
                nombre_mas_alta_femenina = personajes["nombre"]
                bandera_mas_alta_femenina = False
            
    print(f"La femenina mas alta es: {nombre_mas_alta_femenina} y su altura es: {maxima_altura_femenino}") 


#E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
def imprimir_bajo_masculino(lista_personajes):
    minimo_altura_masculino = 0
    bandera_mas_bajo_masculino = True 
    for personajes in lista_personajes:
        if personajes["genero"] == "M":  
            altura = float(personajes["altura"])
            if bandera_mas_bajo_masculino == True or altura < minimo_altura_masculino:
                minimo_altura_masculino = float(personajes["altura"])
                nombre_mas_bajo_masculino = personajes["nombre"]
                bandera_mas_bajo_masculino = False
    
    print(f"El masculino mas bajo es: {nombre_mas_bajo_masculino} y su altura es: {minimo_altura_masculino}")



#F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F

def imprimir_baja_femenino(lista_personajes):
    minima_altura_femenina = 0
    bandera_menor_altura_femenina = True
    for personajes in lista_personajes:
        if personajes["genero"] == "F":  
            altura = float(personajes["altura"])
            if bandera_menor_altura_femenina == True or altura < minima_altura_femenina:
                minima_altura_femenina = float(personajes["altura"])
                nombre_menor_altura_femenina = personajes["nombre"]
                bandera_menor_altura_femenina = False
            
    print(f"La femenina menos alta es: {nombre_menor_altura_femenina} y su altura es: {minima_altura_femenina}") 


#G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
def imprimir_altura_promedio_genero_masculino(lista_personajes):
    acumulador_masculino = 0
    contador_altura_masculino = 0   
    for personajes in lista_personajes: 
        if personajes["genero"] == "M":  
            acumulador_masculino += float(personajes["altura"])
            contador_altura_masculino += 1

    promedio_altura_masculino = acumulador_masculino / contador_altura_masculino
    print(f"El promedio de altura en los superhéroes masculino es: {promedio_altura_masculino}")   
    



#H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
def imprimir_altura_promedio_genero_femenino(lista_personajes):
    acumulador_femenino = 0
    contador_altura_femenino = 0   
    for personajes in lista_personajes: 
        if personajes["genero"] == "F":  # Verificar el género
            acumulador_femenino += float(personajes["altura"])
            contador_altura_femenino += 1
            

    promedio_altura_femenino = acumulador_femenino / contador_altura_femenino
    print(f"El promedio de altura en los superhéroes femenino es: {promedio_altura_femenino}")   



#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def imprimir_tipo_color_ojos(lista_personajes):
    contador_color_ojos = {}
    for personajes in lista_personajes:
        color_ojos = personajes["color_ojos"]
        if color_ojos in contador_color_ojos:
            contador_color_ojos[color_ojos] += 1
        else:
            contador_color_ojos[color_ojos] = 1

    return contador_color_ojos




#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def imprimir_tipo_color_pelos(lista_personajes):
    contador_color_pelo = {}
    for personajes in lista_personajes:
        color_pelo = personajes["color_pelo"]
        if color_pelo in contador_color_pelo:
            contador_color_pelo[color_pelo] += 1
        else:
            contador_color_pelo[color_pelo] = 1

    return contador_color_pelo  



#L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
def agrupacion_tipo_inteligencia(lista_personajes):
    personajes_por_inteligencia = {}
    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"]
        
        if inteligencia in personajes_por_inteligencia:
            personajes_por_inteligencia[inteligencia].append(personaje)
      
        else:
            personajes_por_inteligencia[inteligencia] = [personaje]
   
    for inteligencia, personajes in personajes_por_inteligencia.items():
        print(f"\n Superheroes con inteligencia {inteligencia}: \n ")
        
        for nombre in personajes:
            print(nombre["nombre"])
    return inteligencia, nombre

def pausar():
    import os
    os.system("pause")

def pedir_confirmacion(mensaje:str)->bool:
    respuesta = input(mensaje).lower()
    return respuesta == "si"
