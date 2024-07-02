import pygame
from funciones import *
import random

ventana = crear_ventana()

lista_preguntas = leer_json("lista_preguntas.json")

premios = [
    [1,50000],
    [2,100000],
    [3,150000],
    [4,250000],
    [5,350000],
    [6,475000],
    [7,625000],
    [8,700000],
    [9,875000],
    [10,1000000]
]

clock = pygame.time.Clock()

#Tiempo
tiempo_inicial = 30
inicio_tiempo = pygame.time.get_ticks()

#Ventana
recursos = cargar_recursos()

imagen_actual = recursos["fondo_inicio"]

ventana.blit(imagen_actual, (0,0))

#Eventos
evento_para_iniciar = pygame.USEREVENT
evento_pregunta1 = pygame.USEREVENT + 1

#Preguntas
i_preguntas = 0
respuesta = None
estamos_en_preguntas = False

#Record
record = 0

#Funcionamiento
cambiamos_imagen = False
bandera_seguir = None
mostrar_botones = False
ejecutar = True

cambiar_imagen = lambda: (
    ventana.blit(recursos["fondo_inicio2"], (0, 0)),
    ventana.blit(recursos["gatito_sostiene"], (350, 240)),
    ventana.blit(recursos["mensaje_continuar"], (350, 200))
) if cambiamos_imagen == False else None


while ejecutar:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
          
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.event.post(pygame.event.Event(evento_para_iniciar)) 
            
            pos_x = event.pos[0]
            pos_y = event.pos[1]

            if cambiamos_imagen == True:
                click_continuar(pos_x, pos_y, evento_pregunta1)
                    
                respuesta = obtener_respuestas(pos_x,pos_y)

            if estamos_en_preguntas == True:
                if respuesta == lista_preguntas[i_preguntas]["correcta"]:
                    print ("RESPUESTA CORRECTA")

                    premio_ganado = premios[i_preguntas][1]
                    print(premio_ganado)

                    if premio_ganado > record:
                        record = premio_ganado
                    
                    inicio_tiempo = pygame.time.get_ticks()

                    bandera_seguir = retirarse_seguir(ventana, recursos)
                    if bandera_seguir == True:
                        i_preguntas += 1
                    
                        if i_preguntas >= len(lista_preguntas):
                            mostrar_botones = False
                            estamos_en_preguntas = False
                            ventana.fill(colores.NEGRO)
                            ganaste(ventana, recursos)
                            print("terminaste!")

                    elif bandera_seguir == False:
                        ventana.blit(recursos["fondo_inicio2"], (0, 0))
                        ventana.blit(recursos["retirada"], (310, 200))
                        ventana.blit(recursos["se_retira"], (300, 320))
                        texto_loganado = recursos["fuente_loganado"].render(f"{premio_ganado}", False, colores.NEGRO)
                        ventana.blit(texto_loganado, (400, 240))
                        pygame.display.flip()
                        pygame.time.wait(2000)

                        mostrar_botones = False
                        pygame.display.update()
                        cambiamos_imagen = False
                        guardar_record_en_csv(nombre, premio_ganado, "premios.csv")

                        print(premio_ganado)

                        cambiar_imagen()
                        #click_continuar(pos_x, pos_y, evento_pregunta1)
                        bandera_seguir = True
                        estamos_en_preguntas = False
                        i_preguntas = 0
                        random.shuffle(lista_preguntas)

                    else:
                        ejecutar = False

                elif respuesta != -1:
                    mostrar_botones = False
                    respuesta_incorrecta(ventana, recursos)
                    ventana.blit(recursos["respuesta_incorrecta"], (340, 90)) 
                    pygame.display.update()
                    pygame.time.delay(3000)
                    estamos_en_preguntas = False
                    cambiamos_imagen = False
                    

                    premio_ganado = 0
                    guardar_record_en_csv(nombre, premio_ganado, "premios.csv")
                    cambiar_imagen()
                    i_preguntas = 0
                    random.shuffle(lista_preguntas)
                                            
                    print ("INCORRECTO")
                        
                

        elif event.type == evento_para_iniciar:
            if cambiamos_imagen == False:
                cambiar_imagen()
                cambiamos_imagen = True

        elif event.type == evento_pregunta1:

            nombre = pedir_nombre(ventana,recursos)
            print(nombre)
            mostrar_botones = True
            estamos_en_preguntas = True
            inicio_tiempo = pygame.time.get_ticks()
            
        elif event.type == pygame.QUIT:
            ejecutar = False


    if mostrar_botones == True:
        
        pregunta = lista_preguntas[i_preguntas]["pregunta"]
        respuestas = lista_preguntas[i_preguntas]["respuestas"]
        blitear_preguntas_respuestas(ventana,recursos,pregunta,respuestas)

        mostrar_record(ventana, recursos, record)
        
        tiempo = crear_temporizador(ventana,recursos,inicio_tiempo,tiempo_inicial)
        
        if tiempo <= 0:
            respuesta_incorrecta(ventana, recursos)
            ventana.blit(recursos["tiempo_terminado"], (375, 90))
            cambiar_imagen()
            
            bandera_seguir = True
            estamos_en_preguntas = False
            i_preguntas = 0
            random.shuffle(lista_preguntas)
            print("perdiste")

    clock.tick(30)

    pygame.display.update()

pygame.quit()