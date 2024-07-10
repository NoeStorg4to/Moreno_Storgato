import pygame
import colores
from archivos import *

def cargar_recursos()->dict:
    """
    Carga todos los path de las imagenes y unas fuentes
    Retorna:
    dict, el diccionario cargado 
    """
    recursos = {}
    recursos["fondo_inicio"] = pygame.image.load("Imagenes\INICIO.jpg")
    recursos["fondo_inicio"] = pygame.transform.scale(recursos["fondo_inicio"], (1000, 625))
    recursos["fondo_inicio2"] = pygame.image.load("Imagenes\FONDO_PREGUNTAS.jpg")
    recursos["preguntador"] = pygame.image.load("Imagenes\gatito_presentador1.png")
    recursos["mensaje_continuar"] = pygame.image.load("Imagenes\mensaje_continuar1.png")
    recursos["gatito_sostiene"] = pygame.image.load("Imagenes\gatito_sostiene.png")
    recursos["box_pregunta"] = pygame.image.load("Imagenes\\box_pregunta1.png")
    recursos["box_respuesta"] = pygame.image.load("Imagenes\\box_respuesta.png")
    recursos["reloj"] = pygame.image.load("Imagenes\\reloj1.png")
    recursos["record"] = pygame.image.load("Imagenes\\record.png")
    recursos["gameover"] = pygame.image.load("Imagenes\gatito_gameover.png")
    recursos["ganaste"] = pygame.image.load("Imagenes\ganaste.png")
    recursos["yes"] = pygame.image.load("Imagenes\yes.png")
    recursos["no"] = pygame.image.load("Imagenes\\no.png")
    recursos["continuar"] = pygame.image.load("Imagenes\continuar.png")
    recursos["respuesta_incorrecta"] = pygame.image.load("Imagenes\\respuesta_incorrecta.png")
    recursos["retirada"] = pygame.image.load("Imagenes\\retirada.png")
    recursos["se_retira"] = pygame.image.load("Imagenes\se_retira.png")
    recursos["tiempo_terminado"] = pygame.image.load("Imagenes\\tiempo_terminado.png")
    recursos["gatito_pensando"] = pygame.image.load("Imagenes\gatito_pensando.png")
    recursos["ingrese_nombre"] = pygame.image.load("Imagenes\ingrese_nombre.jpg")
    recursos["nombre_novalido"] = pygame.image.load("Imagenes\\nombre_novalido.jpg")
    recursos["tabla_premios"] = pygame.image.load("Imagenes\\tabla_premio.png")
    recursos["fondo_nombre"] = pygame.image.load("Imagenes\\fondo_nombre.jpeg")
    recursos["fondo_nombre"] = pygame.transform.scale(recursos["fondo_nombre"], (1000, 625))

    recursos["fuente_preguntas"] = pygame.font.SysFont("Comic Sans MS", 15, True)
    recursos["fuente_respuestas"] = pygame.font.SysFont("Comic Sans MS", 30, True)
    recursos["fuente_reloj"] = pygame.font.SysFont("Arial", 40, True)
    recursos["texto_record"] = pygame.font.SysFont("Arial", 20, True)
    recursos["fuente_ganaste"] = pygame.font.SysFont("Comic Sans MS", 40, True)
    recursos["fuente_loganado"] = pygame.font.SysFont("Comic Sans MS", 30, True)
    recursos["fuente_ingreso_nombre"] = pygame.font.SysFont("Comic Sans MS", 25, True)
    recursos["fuente_mensaje_nombre"] = pygame.font.SysFont("Comic Sans MS", 40, True)
    recursos["fuente_mensaje_error"] = pygame.font.SysFont("Comic Sans MS", 30, True)

    return recursos

def obtener_respuestas(pos_x:int,pos_y:int)->int:
    """
    Verifica cual opcion fue seleccionada
    
    Parametros:
    pos_x:int = La posicion de x de donde se hizo click
    pos_y:int = Posicion de y de donde se hizo click
    
    Retorno:
    Int: variable respuesta que indica lo seleccionado  
    
    """
    ancho_box = 250
    largo_box = 81
    
    if pos_x >= 120 and pos_x <= (120 + ancho_box) and pos_y >= 400 and pos_y <= (400 + largo_box):
        respuesta = 0                    
    elif pos_x >= 613 and pos_x <= (613 + ancho_box) and pos_y >= 400 and pos_y <= (400 + largo_box):
        respuesta = 1
    elif pos_x >= 120 and pos_x <= (120 + ancho_box) and pos_y >= 490 and pos_y <= (490 + largo_box):
        respuesta = 2
    elif pos_x >= 613 and pos_x <= (613 + ancho_box) and pos_y >= 490 and pos_y <= (490 + largo_box):
        respuesta = 3
    else:
        respuesta = -1
    
    return respuesta

def blitear_preguntas_respuestas(ventana:pygame.Surface, recursos:dict, pregunta:str, respuestas:int)->None:
    """
    Blitea las preguntas y las respuestas en la pantalla a la hora de jugar, y el estilo
    
    Parametros:
    ventana: donde se va a blitear
    recursos: diccionario de donde se saca las imagenes y fuentes
    pregunta: la pregunta que se este mostrtando
    respuestas: las respuestas
    imagen_actual: el fondo que se este mostrando en el momento
    
    Retorna:
    no retorna nada 
    
    """
    
    ventana.blit(recursos["fondo_inicio2"], (0,0)) 
    ventana.blit(recursos["preguntador"], (370,0))
    ventana.blit(recursos["box_pregunta"], (300, 250))
    ventana.blit(recursos["tabla_premios"], (765, 35))
      
    ventana.blit(recursos["box_respuesta"], (120, 400))
    ventana.blit(recursos["box_respuesta"], (613, 400))
    ventana.blit(recursos["box_respuesta"], (120, 490))
    ventana.blit(recursos["box_respuesta"], (613, 490)) 
        
    respuesta1_pregunta1 = recursos["fuente_respuestas"].render(respuestas[0], False, colores.AZUL)
    ventana.blit(respuesta1_pregunta1, (190, 410))
    respuesta2_pregunta1 = recursos["fuente_respuestas"].render(respuestas[1], False, colores.AZUL)
    ventana.blit(respuesta2_pregunta1, (680, 410))
    respuesta3_pregunta1 = recursos["fuente_respuestas"].render(respuestas[2], False, colores.AZUL)
    ventana.blit(respuesta3_pregunta1, (190, 500))
    respuesta4_pregunta1 = recursos["fuente_respuestas"].render(respuestas[3], False, colores.AZUL)
    ventana.blit(respuesta4_pregunta1, (680, 500))

    pregunta_1 = recursos["fuente_preguntas"].render(pregunta, False, colores.BLANCO, colores.NEGRO)
    ventana.blit(pregunta_1, (330, 290))   


def respuesta_incorrecta (ventana: pygame.Surface, recursos: dict):
    """
    blitea las imagenes si se contesta erroneamente

    Argumentos:
        ventana (pygame.Surface): las imagenes bliteadas
        recursos (dict): en donde se encuentran las imagenes descargadas
    """
    
    ventana.blit(recursos["fondo_inicio2"], (0, 0))
    ventana.blit(recursos["gameover"], (300, 200)) 
    ventana.blit(recursos["respuesta_incorrecta"], (340, 90)) 

def sin_tiempo(ventana: pygame.Surface, recursos: dict):
    """
    blitea las imagenes si se queda sin tiempo

    Argumentos:
        ventana (pygame.Surface): las imagenes bliteadas
        recursos (dict): en donde se encuentran las imagenes descargadas
    """

    ventana.blit(recursos["fondo_inicio2"], (0, 0))
    ventana.blit(recursos["gameover"], (300, 200)) 
    ventana.blit(recursos["tiempo_terminado"], (375, 90))
    