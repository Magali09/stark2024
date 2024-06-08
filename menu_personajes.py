from lista_personajes import *

seguir = "si"

while seguir == "si":
    
    opcion = menu()
    
    match opcion:
        case "1":
            imprimir_nombres(lista_personajes)
        case "2":
            imprimir_nombre_altura(lista_personajes)
        case "3":
            print(imprimir_mas_alto(lista_personajes))
        case "4":
            print(imprimir_mas_bajo(lista_personajes))
        case "5":
            print(imprimir_promedios_personajes(lista_personajes))
        case "6":
            print(imprimir_mas_alto(lista_personajes))
            print(imprimir_mas_bajo(lista_personajes))
        case "7":
            print(imprimir_pesos_personajes(lista_personajes))
        case "8":
            if pedir_confirmacion("¿Confirma salida? si/no: "):
                seguir = "no"
            continue
    pausar()
