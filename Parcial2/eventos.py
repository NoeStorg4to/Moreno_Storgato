import pygame
from funciones import *
from archivos import *


def ganaste(ventana: pygame.Surface, recursos: dict):
    """
    Para poder mostrar en pantalla el mensaje de felicitaciones

    Parámetros: 
    ventana: donde se encuentra la imagen del gatito tirando papeles de felicitación y el mensaje de 'ganaste'
    recursos: diccionario donde se encuentra la imagen del gato y la fuente del texto
    """
    ventana.blit(recursos["ganaste"], (280, 90))
    mensaje_ganaste = "¡Ganaste!"
    texto_ganaste = recursos["fuente_ganaste"].render(mensaje_ganaste, False, colores.BLANCO)
    ventana.blit(texto_ganaste, (410, 50))

def retirarse_seguir (ventana: pygame.Surface, recursos: dict):
    """
    Se le da la opción al usuario de seguir o retirarse, dependiendo de dónde clickee
    
    """
    ventana.blit(recursos["fondo_inicio2"], (0, 0))
    ventana.blit(recursos["continuar"], (350, 100))
    ventana.blit(recursos["gatito_pensando"], (400, 300))
    ventana.blit(recursos["yes"], (300, 200))
    ventana.blit(recursos["no"], (600, 200))
 
    pygame.display.flip()

    ancho= 100
    alto= 90

    ejecutar = True
    while ejecutar:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
               
                if pos_x >= 300 and pos_x <= (300 + ancho) and pos_y >= 200 and pos_y <= (200 + alto):
                    return True  
                elif pos_x >= 600 and pos_x <= 700 and pos_y >= 200 and pos_y <= 290:
                    return False  
            elif event.type == pygame.QUIT:
                return None

def click_continuar (pos_x: int, pos_y: int, evento_pregunta1: int):
    """
    Para encontrar la medida de la superficie en donde se genrará el click para poder disparar el siguiente evento

    Parámetros: 
    pos_x y pos_y: la posición actual del mouse 
    evento_pregunta1: el evento que se va a disparar

    """
 
    if pos_x >= 350 and pos_x <=(350 + 300) and pos_y >= 200 and pos_y <= (200 + 97):
        pygame.event.post(pygame.event.Event(evento_pregunta1))

def retirada (ventana: pygame.Surface, recursos: dict, premio_ganado: int):
    ventana.blit(recursos["fondo_inicio2"], (0, 0))
    ventana.blit(recursos["retirada"], (310, 200))
    ventana.blit(recursos["se_retira"], (300, 320))
    texto_loganado = recursos["fuente_loganado"].render(f"{premio_ganado}", False, colores.NEGRO)
    ventana.blit(texto_loganado, (400, 240))