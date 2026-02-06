import random
from pathlib import Path

FICHERO_FRASES = Path("frases.txt")

def frotar(n_frases: int = 1) -> list:
    if n_frases < 1:
        return []

    with open(FICHERO_FRASES, "r", encoding="utf-8") as f:
        frases = [line.strip() for line in f if line.strip()]

    if not frases:
        return []

    return random.sample(frases, k=min(n_frases, len(frases)))
