from pymongo import MongoClient
import random

MONGO_URI = "mongodb://mongo_bayeta:27017"
DB_NAME = "bayeta"
COLLECTION = "frases_auspiciosas"


def instanciar():
    """
    Conexión con Mongo, devuelve la colección
    """
    cliente = MongoClient(MONGO_URI)
    bd = cliente[DB_NAME]
    return bd[COLLECTION]


def inicializar(fichero="frases.txt"):
    """
    Inserta datos desde fichero si la colección está vacía
    """
    col = instanciar()

    if col.count_documents({}) > 0:
        print("Colección ya inicializada")
        return

    with open(fichero, encoding="utf-8") as f:
        datos = [{"frase": linea.strip()} for linea in f if linea.strip()]

    col.insert_many(datos)
    print("Datos insertados correctamente")


def consultar(n_frases=3):
    """
    Devuelve n frases aleatorias
    """
    col = instanciar()

    if col.count_documents({}) == 0:
        return ["No hay frases disponibles"]

    frases = list(col.aggregate([{'$sample': {'size': n_frases}}]))
    return [f["frase"] for f in frases]
