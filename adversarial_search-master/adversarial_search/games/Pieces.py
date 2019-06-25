from abc import ABC

class Pieces(ABC):
        position =[]
        HP = 0
        moved = False
        alcance = list() #lista de casillas donde cada pieza puede atacar.("la mira", lo que cad pieza ve)
