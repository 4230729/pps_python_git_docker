import random
from pathlib import Path
from mongo_frases import consultar

FICHERO_FRASES = Path("frases.txt")

def frotar():
    return consultar(1)[0]

    with open(FICHERO_FRASES, "r", encoding="utf-8") as f:
        frases = [line.strip() for line in f if line.strip()]

    if not frases:
        return []

    return random.sample(frases, k=min(n_frases, len(frases)))
