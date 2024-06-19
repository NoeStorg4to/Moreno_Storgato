import pygame


pygame.init()

ancho = 1000
altura = 600
dimensiones_ventana = (ancho, altura)

ventana = pygame.display.set_mode(dimensiones_ventana)
pygame.display.set_caption("¿Quien quiere ser millonario?")

logo = pygame.image.load("Parcial 2\Imagenes\icono pesos.png")

pygame.display.set_icon(logo)

fondo = pygame.image.load("Parcial 2\Imagenes\Fondo.jpeg")
fondo = pygame.transform.scale(fondo, dimensiones_ventana)
ventana.blit(fondo, (0,0))


preguntador = pygame.image.load("Parcial 2\Imagenes\preguntadorr.png") 
ventana.blit(preguntador, (0,0))

boton_1 = pygame.image.load("Parcial 2\Imagenes\\botoncito.png")
boton_2 = pygame.image.load("Parcial 2\Imagenes\\botoncito.png")
boton_3 = pygame.image.load("Parcial 2\Imagenes\\botoncito.png")
boton_4 = pygame.image.load("Parcial 2\Imagenes\\botoncito.png")

boton_1 = pygame.transform.scale(boton_1, (645/2, 189/2))
boton_2 = pygame.transform.scale(boton_2, (645/2, 189/2))
boton_3 = pygame.transform.scale(boton_3, (645/2, 189/2))
boton_4 = pygame.transform.scale(boton_4, (645/2, 189/2))

ventana.blit(boton_1, (200, 400))
ventana.blit(boton_2, (600, 800))
ventana.blit(boton_3, (700, 900))



ejecutar = True
while ejecutar:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            ejecutar = False

    pygame.display.update()

pygame.quit()