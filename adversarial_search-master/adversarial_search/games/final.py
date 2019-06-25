# -*- coding: utf-8 -*-
from ..core import Game
from ..utils import coord_id, board_lines, print_board, game_result, cached_property, cached_indexed_property
from abc import ABC, abstractmethod

######### Attributes to calculate##
dmg_k_1 = 1
dmg_k_2 = 1
dmg_k_3 = 1
hp_k = 10

###################################
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


    class Pieces(ABC):
        position =[]
        HP = 0
        moved = False


    class Knight(Pieces):
        DMG_1 = dmg_k_1
        DMG_2 = dmg_k_2
        DMG_3 = dmg_k_3
        HP = hp_k


        def available_moves(self,board):
            ##expreso la posicion en coordenadas, (fila,columna)
            coord = divmod(self.position,9)
            ##busco los posibles movimientos dada la posicion (una o dos casillas en cada direccion ortogonal)
            possible_moves = [(coord[0]+1,coord[1]),(coord[0]+2,coord[1]),(coord[0]-1,coord[1]),(coord[0]-2,coord[1]),(coord[0],coord[1]+1),(coord[0],coord[1]+2),(coord[0],coord[1]-2),(coord[0],coord[1]-1)]
            av_moves=[]
            for x in possible_moves:
                if ((not (x[0] > 8)) & (not (x[1] > 8)) & (board[((x[0] * 9) + x[1])] == 0)):
                    av_moves.append(x)
            return av_moves




