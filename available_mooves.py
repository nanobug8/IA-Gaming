def moves(coord,cant):
        pmoves = [] 
        for x in range(0,5):
                for y in range(0,9):
                        if(manhattan_distance(coord,(x,y)) <= cant):
                                pmoves.append((x,y))
        return pmoves


def manhattan_distance(c1,c2):
        return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def mague_archer_available_moves(board):
        ##expreso la posicion en coordenadas, (fila,columna)
        #Este variable coord luego sera el self.position de la pieza
        coord = (0, 0)
        ##busco los posibles movimientos dada la posicion (una o dos casillas en cada direccio$
        possible_moves = moves(coord,3)
        av_moves = []
        for x in possible_moves:
                available = 1
                for y in board:
                        available = available and cmp(x,y)
                if(available and x[0]>=0 and x[1]>=0):
                        av_moves.append(x)
        print ("available mooves for archer/mague: ", av_moves)
        return av_moves

def knight_available_mooves(board):
        ##expreso la posicion en coordenadas, (fila,columna)
        #Este variable coord luego sera el self.position de la pieza
        coord = (0, 0)
        ##busco los posibles movimientos dada la posicion (una o dos casillas en cada direccio$
        possible_moves = moves(coord,2)
        av_moves = []
        for x in possible_moves:
                available = 1
                for y in board:
                        available = available and cmp(x,y)
                if(available and x[0]>=0 and x[1]>=0):
                        av_moves.append(x)
        print ("avalable mooves for archer or knight: ", av_moves)
        return av_moves

board=[(0,0),(0,1),(1,1)]
mague_archer_available_moves(board)
knight_available_mooves(board)

