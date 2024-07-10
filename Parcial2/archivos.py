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

def leer_json_pregunta(path: str) -> list[dict]:
    """
    Función que lee el json donde se encuentran las preguntas y respuestas, en forma de una lista de diccionarios.
    También lee el récord máximo almacenado en el archivo.

    Parámetros:
    path: Ruta en donde se encuentra el archivo json.

    Retorna:
    Una tupla que contiene el récord máximo y la lista de diccionario del json.
    """
    with open(path, "r") as archivo:
        datos = json.load(archivo)
    
    lista_preguntas = datos.get("preguntas", [])

    return lista_preguntas

def leer_json_record(path: str) -> list[dict]:
    """
    Función que lee el json donde se encuentran las preguntas y respuestas, en forma de una lista de diccionarios.
    También lee el récord máximo almacenado en el archivo.

    Parámetros:
    path: Ruta en donde se encuentra el archivo json.

    Retorna:
    Una tupla que contiene el récord máximo y la lista de diccionario del json.
    """
    with open(path, "r") as archivo:
        datos = json.load(archivo)
    
    record_maximo = datos.get("record_maximo")

    return record_maximo


def guardar_record_maximo(record_maximo: int, path: str):
    """
    guarda el record maximo del premio ganados

    Argumentos:
        record_maximo (int):el record maximo de dinero ganado
        path (str): la ruta del archivo en donde se guardan los records
    """

    data = leer_json(path)
    data["record_maximo"] = record_maximo
    with open(path, "w") as archivo:
        json.dump(data, archivo, indent=4)


def guardar_record_en_csv(nombre, premio_ganado, path: str):
    """
    guarda el ultimo record con el nombre

    Argumentos:
        nombre (_type_): nombre que se pide al principio
        premio_ganado (_type_): cuanto dinero acumulo
        path (str): ruta del archivo donde se guarda la info
    """

    archivo = open(path, mode='a', newline='')
    archivo.write(f"{nombre},{premio_ganado}\n")
    archivo.close()
