from adversarial_search.games.Pieces import *

#######Attributes to calculate######
dmg_k_1 = 1
dmg_k_2 = 1
dmg_k_3 = 1
hp_k = 10

####################################



class Knight(Pieces):
        DMG_1 = dmg_k_1
        DMG_2 = dmg_k_2
        DMG_3 = dmg_k_3
        HP = hp_k


        def available_moves(self, board):
                ##expreso la posicion en coordenadas, (fila,columna)
                coord = divmod(self.position, 9)
                ##busco los posibles movimientos dada la posicion (una o dos casillas en cada direccion ortogonal)
                possible_moves = [(coord[0] + 1, coord[1]), (coord[0] + 2, coord[1]), (coord[0] - 1, coord[1]),
                                  (coord[0] - 2, coord[1]), (coord[0], coord[1] + 1), (coord[0], coord[1] + 2),
                                  (coord[0], coord[1] - 2), (coord[0], coord[1] - 1)]
                av_moves = []
                for x in possible_moves:
                        if ((not (x[0] > 8)) & (not (x[1] > 8)) & (board[((x[0] * 9) + x[1])] == 0)):
                                av_moves.append(x)
                return av_moves

