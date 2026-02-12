from mongo_frases import consultar, insertar


def frotar():
    return consultar(1)[0]


def añadir_frases(frases):
    return insertar(frases)
