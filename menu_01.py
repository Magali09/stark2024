from lista_personajes01 import *

seguir = "si"

while seguir == "si":
    
    opcion = menu()
    
    match opcion:
        case "1":
            imprimir_genero_masculino(lista_personajes)
           
        case "2":
            imprimir_genero_femenino(lista_personajes)
            
        case "3":
            imprimir_alto_masculino(lista_personajes)
            
        case "4":
           imprimir_alto_femenino(lista_personajes)
            
        case "5":
           imprimir_bajo_masculino(lista_personajes)
           
        case "6":
            imprimir_baja_femenino(lista_personajes)
           
        case "7":
           imprimir_altura_promedio_genero_masculino(lista_personajes)
            
        case"8":
            imprimir_altura_promedio_genero_femenino(lista_personajes)
            
        case "9":
            imprimir_alto_masculino(lista_personajes)  
            imprimir_alto_femenino(lista_personajes)
            imprimir_bajo_masculino(lista_personajes)
            imprimir_baja_femenino(lista_personajes)
        case "10":
            
            respuesta = imprimir_tipo_color_ojos(lista_personajes)
            print(f"La cantidad de colores de ojos que hay es: \n{respuesta}")
            
        case "11":
            respuesta = imprimir_tipo_color_pelos(lista_personajes)
            print(respuesta)
            
        case "12":
            tipo_inteligencia = agrupacion_tipo_inteligencia(lista_personajes)   
            print(f"Número de superhéroes con cada tipo de inteligencia: {tipo_inteligencia}")
        case "13":
            print(imprimir_tipo_color_ojos(lista_personajes))   
        case "14":
            print(imprimir_tipo_color_pelos(lista_personajes))
        case "15":
            print(agrupacion_tipo_inteligencia(lista_personajes))
        
        case "16":
            if pedir_confirmacion("¿Confirma salida? si/no: "):
                seguir = "no"
            continue
            
    pausar()                        
                    
                    
    
    
       
         
  
            

    
            
            
            
        
            
     
                