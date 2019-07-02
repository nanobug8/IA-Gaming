import itertools


turno = 2
obstaculos = [(1,4),(3,3),(5,2),(0,7)]

KNIGHT = 1
MAGUE = 2
ARCHER = 3

ATTACK = 1
DO_NOT_ATTACK =0


def moves(coord,cant):
        pmoves = []
        for x in range(0,5):
                for y in range(0,9):
                        if(manhattan_distance(coord,(x,y)) <= cant):
                                pmoves.append((x,y))
        return pmoves


def manhattan_distance(c1,c2):
        return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def mague_available_moves(board):
        ##expreso la posicion en coordenadas, (fila,columna)
        #Este variable coord luego sera el self.position de la pieza
        coord = board[1][0]
        ##busco los posibles movimientos dada la posicion (una o dos casillas en cada direccio$
        possible_moves = moves(coord,3)
        av_moves = []
        for x in possible_moves:
                available = 1
                for y in board:
                        available = available and cmp(x,y[0])
                if(available and x[0]>=0 and x[1]>=0):
                        av_moves.append(x)
        ret = [item for item in av_moves if item not in obstaculos]
        ret.append(coord)
        print ("available moves for mague: ", ret)
        return ret


def archer_available_moves(board):
        ##expreso la posicion en coordenadas, (fila,columna)
        #Este variable coord luego sera el self.position de la pieza
        coord = board[2][0]
        ##busco los posibles movimientos dada la posicion (una o dos casillas en cada direccio$
        possible_moves = moves(coord,3)
        av_moves = []
        for x in possible_moves:
                available = 1
                for y in board:
                        available = available and cmp(x,y[0])
                if(available and x[0]>=0 and x[1]>=0):
                        av_moves.append(x)
        ret = [item for item in av_moves if item not in obstaculos]
        ret.append(coord)
        print ("available moves for mague: ", ret)
        return ret


def knight_available_moves(board):
        ##expreso la posicion en coordenadas, (fila,columna)
        #Este variable coord luego sera el self.position de la pieza
        coord = board[0][0]
        ##busco los posibles movimientos dada la posicion (una o dos casillas en cada direccio$
        possible_moves = moves(coord,2)
        av_moves = []
        for x in possible_moves:
                available = 1
                for y in board:
                        available = available and cmp(x,y[0])
                if(available and x[0]>=0 and x[1]>=0):
                        av_moves.append(x)
        ret = [item for item in av_moves if item not in obstaculos]
        ret.append(coord)

        print("available moves for knight: ", ret)

        return ret


def available_pieces(board):
        pieces = []
        offset = 0 if turno == 1 else 3
        for i in range(0,3):
                if board[offset + i][1] > 0:
                        pieces.append(offset + i)
        return pieces

def available_pieces_nemesis(board):
        pieces = []
        offset = 3 if turno == 1 else 0
        for i in range(0,3):
                if board[offset + i][1] > 0:
                        pieces.append(offset + i)
        return pieces



def posible_action(estado):
        for element in itertools.product(*estado):
                print(element)

def cmp(a, b):
    return (a > b) - (a < b)


def tucutucutucu(board):
        tuculist = []

        available_positions_knight = knight_available_moves(board)
        available_positions_archer = archer_available_moves(board)
        available_positions_mague = mague_available_moves(board)

        opponent = available_pieces_nemesis(board)

        movimientos = Union(tuculist, itertools.product([KNIGHT], available_positions_knight,[DO_NOT_ATTACK,ATTACK],opponent))
        movimientos = Union(movimientos, itertools.product([MAGUE],available_positions_mague,[DO_NOT_ATTACK,ATTACK],opponent))

        movimientos = Union(movimientos,itertools.product([ARCHER],available_positions_archer,[DO_NOT_ATTACK,ATTACK],opponent))

        print('SE MUEVE SE MUEVE SE JUEGA SE JUEGA: ', movimientos)


def Union(lista, movements):
        for element in movements:
                lista.append(element)
        return lista




board = [[(0,0),0],[(4,5),10],[(3,6),10],[(1,0),10],[(8,8),10],[(6,7),10]]


tucutucutucu(board)
