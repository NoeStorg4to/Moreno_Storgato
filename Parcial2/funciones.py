import pygame
import colores


def pedir_nombre(ventana: pygame.Surface, recursos: dict):
    """
    pide el nombre para luego guardarlo en un csv

    Argumentos:
        ventana (pygame.Surface): - blitea el box donde se ingresara el nombre
                                - blitea el fondo
        recursos (dict): trae las imagenes

    Returns:
        texto: el nombre
    """

    pygame.font.init()
    texto = ""
    pedir_nombre = True

    error_mensaje = ""

    while pedir_nombre:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if texto.isalpha() and len(texto) <= 20:
                        pedir_nombre = False
                    else:
                        error_mensaje = ventana.blit(recursos["nombre_novalido"], (200, 350))
                elif event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                else:
                    if len(texto) < 20:
                        texto += event.unicode

        ventana.blit(recursos["fondo_nombre"], (0, 0))
        ventana.blit(recursos["ingrese_nombre"], (280, 50))
        ventana.blit(recursos["box_respuesta"], (385, 300))
        texto_superficie = recursos["fuente_ingreso_nombre"].render(texto, True, colores.AZUL)
        ventana.blit(texto_superficie, (400, 300))

        if error_mensaje:
            ventana.blit(recursos["nombre_novalido"], (360, 430))
        
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

    texto_tiempo = recursos["fuente_reloj"].render(f"{str(tiempo_restante).zfill(2)}", False, colores.BLANCO)
    ventana.blit(recursos["reloj"],(460,450))
    ventana.blit(texto_tiempo, (480,467))
    return tiempo_restante  
    
def mostrar_record (ventana: pygame.Surface, recursos: dict, record_maximo: int) -> None:
    """
    Muestra el dinero que se va ganando en pantalla.

    Parámetros: 
    ventana: donde se muestra la surface que se usa para el record y se va a mostrar el monto
    recursos: diccionario con le path de la imagen 'record' y el texto del monto
    record: el monto que se va ganando

    Retorna:
    Nada
    """

    ventana.blit(recursos["record"], (90, 90))
    record_mostrado = recursos["texto_record"].render(f"{record_maximo}", False, colores.NEGRO)
    ventana.blit(record_mostrado, (100, 130))

def tabla_premios (posicion_flecha: pygame.Rect, accion: str):
    """
    - Maneja el movimiento de la flecha

    Argumentos:
        posicion_flecha (pygame.Rect): la posicion de la flecha cargada en formato Rect
        accion (str): le paso por parametro si quiero que baje o se reinicie, dependiendo del evento
    """

    decremento = 30
    
    if accion == "bajar":
        posicion_flecha.y += decremento
    elif accion == "reiniciar":
        posicion_flecha.y = 0

def cargar_flecha_rect ():
    """
    - Descarga la imagen de la flecha y la tranforma en un Rect

    Returns:
        flecha, posicion_flecha: devuelve la imagen y la posicion de la flecha
    """

    flecha = pygame.image.load("Imagenes\\flecha.png")
    posicion_flecha = flecha.get_rect()

    posicion_flecha.topleft = (720, 0)

    return flecha, posicion_flecha

