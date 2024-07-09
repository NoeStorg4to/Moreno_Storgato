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