import pygame
import colores
import json


def leer_json (path:str) -> list[dict]:
    """
    Funcion que lee el json donde se encuentran las preguntas y respuestas, en forma de una lista de diccionarios.

    Parámetros: 
    path en donde se encuentra el archivo json.

    Retorna:
    La lista de diccionario del json.
    """
    archivo = open (path, "r")
    retorno = json.load(archivo)
    archivo.close()

    return retorno

def guardar_record_en_csv(nombre, premio_ganado, path: str):

    archivo = open(path, mode='a', newline='')
    archivo.write(f"{nombre},{premio_ganado}\n")
    archivo.close()

def pedir_nombre(ventana: pygame.Surface, recursos: dict):
    pygame.font.init()
    texto = ""
    pedir_nombre = True

    mensaje = "Ingrese su nombre por teclado:"
    mensaje_superficie = recursos["fuente_mensaje_nombre"] .render(mensaje, True, colores.NEGRO)

    error_mensaje = ""

    while pedir_nombre:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Validar que el nombre contenga solo caracteres y tenga longitud máxima de 20
                    if texto.isalpha() and len(texto) <= 20:
                        pedir_nombre = False
                    else:
                        error_mensaje = "Nombre no válido. Use solo letras y máx. 20 caracteres."
                elif event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                else:
                    if len(texto) < 20:
                        texto += event.unicode

        ventana.fill(colores.BLANCO)
        
        ventana.blit(mensaje_superficie, (100, 50))

        texto_superficie = recursos["fuente_ingreso_nombre"].render(texto, True, colores.AZUL)
        ventana.blit(texto_superficie, (100, 150))

        if error_mensaje:
            error_superficie = recursos["fuente_mensaje_error"].render(error_mensaje, True, colores.ROSITA)
            ventana.blit(error_superficie, (100, 250))
        
        pygame.display.flip()

    return texto


nombre =""


def crear_ventana()-> pygame.Surface:
    """
    Se crea la ventana
    
    Retorna:
    Un surface, la ventana
    
    """
    pygame.init()

    ANCHO = 1000
    ALTURA = 625
    
    DIMENSIONES_VENTANA = (ANCHO, ALTURA)

    ventana = pygame.display.set_mode(DIMENSIONES_VENTANA)
    pygame.display.set_caption("¿Quien quiere ser millonario?")
    
    
    return ventana




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

    recursos["fuente_preguntas"] = pygame.font.SysFont("Comic Sans MS", 15, True)
    recursos["fuente_respuestas"] = pygame.font.SysFont("Comic Sans MS", 30, True)
    recursos["fuente_reloj"] = pygame.font.SysFont("Arial", 40, True)
    recursos["texto_record"] = pygame.font.SysFont("Arial", 20, True)
    recursos["fuente_ganaste"] = pygame.font.SysFont("Comic Sans MS", 40, True)
    recursos["fuente_loganado"] = pygame.font.SysFont("Comic Sans MS", 30, True)
    recursos["fuente_ingreso_nombre"] = pygame.font.SysFont("Comic Sans MS", 50, True)
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
    


def crear_temporizador(ventana:pygame.Surface, recursos:dict, inicio_tiempo:int, tiempo_inicial:int)->int:
    """
    Genera el temporizador, lo renderiza y lo muestra en pantalla
    
    Parametros:
    ventana: para mostrarun reloj y el temporizador en pantalla
    recursos: un diccionario con las path del reloj y la fuente
    inicio_tiempo: cuanto lleva contado desde que inicio el juego
    tiempo_inicial: cuanto tiempo tiene el temporizador para llegar a 0
    
    Retorna:
    int,cuanto tiempo queda
    
    """
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = (tiempo_actual - inicio_tiempo) // 1000
    tiempo_restante = tiempo_inicial - tiempo_transcurrido
    if tiempo_restante < 0:
        tiempo_restante = 0

    texto_tiempo = recursos["fuente_reloj"].render(f"{str(tiempo_restante).zfill(2)}", False, colores.BLANCO,colores.NEGRO)
    ventana.blit(recursos["reloj"],(460,450))
    ventana.blit(texto_tiempo, (480,467))
    return tiempo_restante  
    
def mostrar_record (ventana: pygame.Surface, recursos: dict, record: int) -> None:

    ventana.blit(recursos["record"], (90, 90))
    record_mostrado = recursos["texto_record"].render(f"{record}", False, colores.NEGRO)
    ventana.blit(record_mostrado, (100, 130))

def respuesta_incorrecta (ventana: pygame.Surface, recursos: dict):
    
    ventana.blit(recursos["fondo_inicio2"], (0, 0))
    ventana.blit(recursos["gameover"], (300, 200)) 

def click_continuar (pos_x: int, pos_y: int, evento_pregunta1: int):
 
    if pos_x >= 350 and pos_x <=(350 + 300) and pos_y >= 200 and pos_y <= (200 + 97):
        pygame.event.post(pygame.event.Event(evento_pregunta1))

def ganaste(ventana: pygame.Surface, recursos: dict):
    ventana.blit(recursos["ganaste"], (300, 90))
    mensaje_ganaste = "¡Ganaste!"
    texto_ganaste = recursos["fuente_ganaste"].render(mensaje_ganaste, False, colores.BLANCO)
    ventana.blit(texto_ganaste, (350, 90))

def retirarse_seguir (ventana: pygame.Surface, recursos: dict):

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
