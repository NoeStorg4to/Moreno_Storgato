import pygame
import colores

pygame.init()

ancho = 1000
altura = 625
dimensiones_ventana = (ancho, altura)

ventana = pygame.display.set_mode(dimensiones_ventana)
pygame.display.set_caption("¿Quien quiere ser millonario?")

logo = pygame.image.load("Parcial 2\Imagenes\icono pesos.png")

pygame.display.set_icon(logo)

fondo_incio1 = pygame.image.load("Parcial 2\Imagenes\INICIO.jpg")
fondo_incio1 = pygame.transform.scale(fondo_incio1, dimensiones_ventana)

# boton_play = pygame.image.load("Parcial 2\Imagenes\plaay2.png")
# ventana.blit(boton_play, (440,290))
# ancho_boton_play = 123
# alto_boton_play = 150
# ventana.blit(pantalla, (50, 50))

fondo_inicio2 = pygame.image.load("Parcial 2\Imagenes\FONDO_PREGUNTAS.jpg")

preguntador = pygame.image.load("Parcial 2\Imagenes\gatito_presentador1.png") 

mensaje_continuar = pygame.image.load("Parcial 2\Imagenes\mensaje_continuar1.png")

gatito_sostiene = pygame.image.load("Parcial 2\Imagenes\gatito_sostiene.png")

box_pregunta = pygame.image.load("Parcial 2\Imagenes\\box_pregunta1.png")

box_respuesta1 = pygame.image.load("Parcial 2\Imagenes\\box_respuesta.png")
ancho_box = 250
largo_box = 81

box_1 = pygame.Rect(120, 400, 250, 81)

# largo_elipse = 80
# ancho_elipse = 280
fuente_2 = pygame.font.SysFont("Comic Sans MS", 20, True)
pregunta = "¿Qué animal guarda comida en sus cachetes?"
fuente = pygame.font.SysFont("Comic Sans MS", 30, True)
respuesta_1 = "Ardilla"
respuesta_2 = "Perro"
respuesta_3 = "Canguro"
respuesta_4 = "Pato"

fuente_reloj = pygame.font.SysFont("Arial", 40, True)

clock = pygame.time.Clock()
tiempo_inicial = 0
tiempo_restante = 30
tiempo_actual = pygame.time.get_ticks()

ventana.blit(fondo_incio1, (0,0))

evento_para_iniciar = pygame.USEREVENT
evento_pregunta1 = pygame.USEREVENT + 1
evento_elegir_respuesta = pygame.USEREVENT + 2
 

bandera = False
mostrar_botones = False
ejecutar = True
while ejecutar:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.event.post(pygame.event.Event(evento_para_iniciar)) 
            pygame.event.post(pygame.event.Event(evento_pregunta1))
            pos_x = event.pos[0]
            pos_y = event.pos[1]
            if pos_x >= 120 and pos_x <= (120 + ancho_box) and pos_y >= 400 and pos_y <= (400 + largo_box):
                pygame.event.post(pygame.event.Event(evento_elegir_respuesta))
            elif pos_x >= 613 and pos_x <= (613 + ancho_box) and pos_y >= 400 and pos_y <= (400 + largo_box):
                
                print("RESPUESTA INCORRECTA")
            elif pos_x >= 120 and pos_x <= (120 + ancho_box) and pos_y >= 490 and pos_y <= (490 + largo_box):
                print("RESPUESTA INCORRECTA")
            elif pos_x >= 613 and pos_x <= (613 + ancho_box) and pos_y >= 490 and pos_y <= (490 + largo_box):
                print("RESPUESTA INCORRECTA")

        elif event.type == evento_elegir_respuesta:

            print("RESPUESTA CORRECTA")
            
        elif event.type == evento_para_iniciar:
            ventana.blit(fondo_inicio2, (0,0))
            ventana.blit(gatito_sostiene, (350,240))
            ventana.blit(mensaje_continuar, (350,200))

        elif event.type == evento_pregunta1:
            ventana.blit(fondo_inicio2, (0,0)) 
            ventana.blit(preguntador, (370,0))
            ventana.blit(box_pregunta, (300, 250))
            mostrar_botones = True
            bandera = True        
                        
        elif event.type == pygame.QUIT:
            ejecutar = False
    
    if bandera == True:
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        temporizador = tiempo_restante - int(tiempo_transcurrido * 0.001)
        imagen_reloj = pygame.image.load("Parcial 2\Imagenes\\reloj1.png")
        ventana.blit(imagen_reloj, (460,450))
        reloj = fuente_reloj.render(f"{temporizador}", False, colores.BLANCO, colores.NEGRO)
        ventana.blit(reloj, (480,467))

    if mostrar_botones == True:
        ventana.blit(box_respuesta1, (120, 400))
        ventana.blit(box_respuesta1, (613, 400))
        ventana.blit(box_respuesta1, (120, 490))
        ventana.blit(box_respuesta1, (613, 490))    
        boton_1 = fuente.render(respuesta_1, False, colores.AZUL)
        ventana.blit(boton_1, (190, 410))
        boton_2 = fuente.render(respuesta_2, False, colores.AZUL)
        ventana.blit(boton_2, (695, 410))
        boton_3 = fuente.render(respuesta_3, False, colores.AZUL)
        ventana.blit(boton_3, (190, 500))
        boton_4 = fuente.render(respuesta_4, False, colores.AZUL)
        ventana.blit(boton_4, (700, 500))
        pregunta_1 = fuente_2.render(pregunta, False, colores.BLANCO, colores.NEGRO)
        ventana.blit(pregunta_1, (284, 275))

        
    
    # else:
    #     ventana.blit(fondo_incio1, (0,0))


          
        #print(f"{pos_x}, {pos_y}") 
  

        #if pos_x >= x_elipse and pos_x <= (x_elipse + ancho_elipse) and pos_y >= y_elipse and pos_y <= (y_elipse + largo_elipse):

    
    
    #print (f"{(tiempo_transcurrido / 1000):.02f}")

    clock.tick(30)

    pygame.display.update()

pygame.quit()