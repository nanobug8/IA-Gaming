# -*- coding: utf-8 -*-
from .Pieces import *
from .Knihgt import *

# Imports del resto de las piezas

from ..core import Game
from ..utils import coord_id, board_lines, print_board, game_result, cached_property, cached_indexed_property
from abc import ABC, abstractmethod



class Final(Game):
    PLAYERS = ('Good', 'Bad')
    ###### Lista de 45 posiciones (filas de la matriz tablero concatenadas) ###############
    ###### Si el valor es -1, la casilla contiene un obstáculo, un 0 significa disponible, y un 1 es una pieza
    initial_board = [0,-1,0,0,0,0,0,0,0,1,0,0,-1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,-1,0,0,1,0,0,0,0,0,0,0,-1,0]

    def __init__(self, board=initial_board, enabled=0):
        Game.__init__(self, *Final.PLAYERS)
        self.board = board
        self.enabled = enabled

    class _Move(int):
        def __str__(self):
            return coord_id(*divmod(self, 9))

    def active_player(self):
        return self.players[self.enabled]










