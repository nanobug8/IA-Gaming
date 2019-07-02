# -*- coding: utf-8 -*-

# Imports del resto de las piezas

from adversarial_search.core import Game
from adversarial_search.utils import coord_id, board_lines, print_board, game_result, cached_property, cached_indexed_property
from abc import ABC, abstractmethod



class Final(Game):
    PLAYERS = ('Good', 'Bad')
    ###### Lista de 45 posiciones (filas de la matriz tablero concatenadas) ###############
    ###### Si el valor es -1, la casilla contiene un obstáculo, un 0 significa disponible, y un 1 es una pieza
    initial_board=[[(0,1),30],[(0,2),30],[(0,3),30],[(8,1),30],[(8,2),30],[(8,3),30]]

    def __init__(self, board=initial_board, enabled=0):
        Game.__init__(self, *Final.PLAYERS)
        self.board = board
        self.enabled = enabled

        print(self.enabled)

    def _mooves(self):
        def __str__(self):
            return coord_id(*divmod(self, 9))

    def active_player(self):
        return self.players[self.enabled]
