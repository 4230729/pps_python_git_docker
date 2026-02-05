import random

_FRASES = []

def frotar(n_frases: int = 1) -> list:

    if n_frases < 1:
        return []

    return random.sample(_FRASES, k=min(n_frases, len(_FRASES)))
