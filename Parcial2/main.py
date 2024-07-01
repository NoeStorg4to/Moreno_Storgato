import pygame
import json
from funciones import *

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
mostrar_botones = False
ejecutar = True

while ejecutar:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
          
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.event.post(pygame.event.Event(evento_para_iniciar)) 
            
            pos_x = event.pos[0]
            pos_y = event.pos[1]
            
            if imagen_actual == recursos["fondo_inicio2"]:
                # if pos_x >= 350 and pos_x <=(350 + 300) and pos_y >= 200 and pos_y <= (200 + 97):
                #     pygame.event.post(pygame.event.Event(evento_pregunta1))
                click_continuar(pos_x, pos_y, evento_pregunta1)
                    
                respuesta = obtener_respuestas(pos_x,pos_y)

            if estamos_en_preguntas == True:
                if respuesta == lista_preguntas[i_preguntas]["correcta"]:
                    mostrar_botones = False
                    estamos_en_preguntas = False
                    
                    retirarse_seguir(ventana, recursos, pos_x, pos_y, evento_pregunta1)
                    print ("RESPUESTA CORRECTA")
                    
                    premio_ganado = premios[i_preguntas][1]
                    print(premio_ganado)
                    if premio_ganado > record:
                        record = premio_ganado
                    
                    inicio_tiempo = pygame.time.get_ticks()
                    if i_preguntas < len(lista_preguntas)-1:
                        i_preguntas += 1
                    else:
                        mostrar_botones = False
                        estamos_en_preguntas = False
                        ventana.fill(colores.NEGRO)
                        ganaste(ventana, recursos)
                        print("terminaste!")
                    
                    
                elif respuesta != -1:
                    mostrar_botones = False
                    ventana.blit(recursos["respuesta_incorrecta"], (300, 90)) 
                    respuesta_incorrecta(ventana, recursos)
                    pygame.display.update()
                    pygame.time.delay(3000)
                    estamos_en_preguntas = False
                    premio_ganado = 0
                    guardar_record_en_csv(premio_ganado)
                    cambiar_ventanas(ventana, recursos)
                    click_continuar(pos_x, pos_y, evento_pregunta1)
                    i_preguntas = 0
                                            
                    print ("INCORRECTO")
                        
                

        elif event.type == evento_para_iniciar:
            if imagen_actual == recursos["fondo_inicio"]:
                imagen_actual = recursos["fondo_inicio2"]
                ventana.blit(imagen_actual, (0,0))
                ventana.blit(recursos["gatito_sostiene"], (350,240))
                ventana.blit(recursos["mensaje_continuar"], (350,200))

        elif event.type == evento_pregunta1:
            mostrar_botones = True
            estamos_en_preguntas = True
            inicio_tiempo = pygame.time.get_ticks()
            
        elif event.type == pygame.QUIT:
            ejecutar = False


    if mostrar_botones == True:
        
        pregunta = lista_preguntas[i_preguntas]["pregunta"]
        respuestas = lista_preguntas[i_preguntas]["respuestas"]
        blitear_preguntas_respuestas(ventana,recursos,pregunta,respuestas,imagen_actual)

        mostrar_record(ventana, recursos, record)
        
        tiempo = crear_temporizador(ventana,recursos,inicio_tiempo,tiempo_inicial)
        
        if tiempo <= 0:
            respuesta_incorrecta(ventana, recursos)
            ventana.blit(recursos["tiempo_terminado"], (300, 90))
            print("perdiste")

    clock.tick(30)

    pygame.display.update()

pygame.quit()