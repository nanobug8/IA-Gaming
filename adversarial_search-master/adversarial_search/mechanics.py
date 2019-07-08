from adversarial_search.classes import piece, motion, attack, move
#from KMA import KMA

k_hp = 30
m_hp = 30
a_hp = 30
k_dmg_1 = 10
k_dmg_2 = 7
k_dmg_3 = 5
m_dmg_1 = -5
m_dmg_2 = 3
m_dist_1 = 4
a_dmg_1 = 6
a_dmg_2 = 4
a_dist_1 = 4
knight_1 = piece(1, 1, k_hp, (0, 3))
mage_1 = piece(1, 2, m_hp, (0, 2))
archer_1 = piece(1, 3, a_hp, (0, 1))
knight_2 = piece(2, 1, k_hp, (8, 3))
mage_2 = piece(2, 2, m_hp, (8, 2))
archer_2 = piece(2, 3, a_hp, (8, 1))
obstacles = [(2, 4), (3, 3), (5, 1), (6, 0)]
initial_board = [knight_1,mage_1,archer_1,knight_2,mage_2,archer_2]

def manhattan_distance(pos1,pos2):
    return (abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1]))

def neighbours(pos):
    x=pos[0]
    y=pos[1]
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

def find_piece(board,position):
    exists = False
    for pieces in board:
        if pieces.position == position:
            exists = True
            return exists
    return False

def get_position_list (board):
    positions = []
    for piece in board:
        positions.append(piece.position)
    return positions

def surroundings (pos):
    neighbors = lambda x, y: [(x2, y2) for x2 in range(x - 1, x + 2)
                              for y2 in range(y - 1, y + 2)
                              if (-1 < x <= 8 and
                                  -1 < y <= 4 and
                                  (x != x2 or y != y2) and
                                  (0 <= x2 <= 8) and
                                  (0 <= y2 <= 4))]
    return  neighbors(pos[0],pos[1])

#Verlifies if a given position is occuppied (either by an obstacle or a token)
#Retreturns true if the position is free
def check_pos (board,position,obstacles=obstacles):
    if ((not(position in get_position_list(board)))&(not(position in obstacles))&((position[0]>=0)&(position[0]<=8)&(position[1]>=0)&(position[1]<=4))):
        return True
    else:
        return False

#Checks if there's an obstacle or token between two pieces that share an axis
#Attribute axis is the non-shared component between the coordinates
#Returns true if the way is covered
def obstacle_in_the_way(board,coord1,coord2,axis):
    ok = False
    lowest = min(coord1[axis],coord2[axis])
    highest = max(coord1[axis],coord2[axis])
    for i in range (lowest,highest):
        if (axis==0)& (not check_pos(board,(i,coord1[1]))):
            ok = True
            return ok
        if (axis==1)& (not check_pos(board,(coord1[0],i))):
            ok = True
            return ok
    return ok

def enemy_in_position(board,attacked_position,attacking_piece):
    ok = False
    for other_piece in board:
        if (other_piece.team!=attacking_piece.team):
            if (other_piece.position==attacked_position):
                ok = True
    return ok


def knight_motion(board,piece):
    k_motion=[]
    x,y = piece.position
    ## Charge movement
    knight_charge = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
    for cell in knight_charge:
        if check_pos(board,cell):
            one_motion = motion(piece,cell)
            k_motion.append(one_motion)
    ## Walking movement
    for cell in surroundings((x,y)):
        if check_pos(board,cell):
            one_motion = motion(piece,cell)
            k_motion.append(one_motion)
    ## Steady movement
    steady_motion=motion(piece,piece.position)
    k_motion.append(steady_motion)
    return k_motion

def archer_motion(board,piece):
    a_motion=[]
    steady_motion = motion(piece,piece.position)
    a_motion.append(steady_motion)
    for i in range(9):
        for j in range (5):
            if ((check_pos(board,(i,j)))&(manhattan_distance(piece.position,(i,j))<=3)):
                one_motion = motion(piece,(i,j))
                a_motion.append(one_motion)
    return a_motion

def mage_motion(board,piece):
    m_motion=[]
    steady_motion = motion(piece,piece.position)
    m_motion.append(steady_motion)
    for i in range(9):
        for j in range (5):
            if ((check_pos(board,(i,j)))&(manhattan_distance(piece.position,(i,j))<=3)):
                one_motion = motion(piece,(i,j))
                m_motion.append(one_motion)
    return m_motion

def available_motion(board,enabled):
    av_motion=[]
    if enabled==1:
        team=1
    else:
        team=2
    for token in board:
        if token.team==team:
            if token.type==1:
                for k_motion in knight_motion(board,token):
                    av_motion.append(k_motion)
            if token.type==3:
                for a_motion in archer_motion(board,token):
                    av_motion.append(a_motion)
            if token.type==2:
                for m_motion in mage_motion(board,token):
                    av_motion.append(m_motion)
    return av_motion

def knight_charge(board,motion,i_pos,f_pos):
    one_attack=attack(damaged=None,dmg_points=0)
    if (f_pos[0]-i_pos[0]==2):
        for index in range(len(board)):
            if (board[index].position == (f_pos[0]+1,f_pos[1]))&(board[index].team!=motion.piece.team):
                one_attack=attack(index,k_dmg_1)
    if (f_pos[0]-i_pos[0]==-2):
        for index in range(len(board)):
            if (board[index].position == (f_pos[0]-1,f_pos[1]))&(board[index].team!=motion.piece.team):
                one_attack=attack(index,k_dmg_1)
    if (f_pos[1]-i_pos[1]==2):
        for index in range(len(board)):
            if (board[index].position == (f_pos[0],f_pos[1]+1))&(board[index].team!=motion.piece.team):
                one_attack=attack(index,k_dmg_1)
    if (f_pos[1]-i_pos[1]==-2):
        for index in range(len(board)):
            if (board[index].position == (f_pos[0],f_pos[1]-1))&(board[index].team!=motion.piece.team):
                one_attack=attack(index,k_dmg_1)
    return one_attack


def knight_attack(board,motion):
    total_moves = []
    init_pos = motion.piece.position
    fin_pos = motion.final_position
    pos_diff = max(abs(init_pos[0]-fin_pos[0]),abs(init_pos[1]-fin_pos[1]))
    ##Charge attack
    if pos_diff==2:
        k_attack=move(motion,knight_charge(board,motion,init_pos,fin_pos))
        total_moves.append(k_attack)
    ##Walking attack
    if pos_diff==1:
        for cell in neighbours(motion.final_position):
            for index in range(len(board)):
                if (board[index].position == cell)&(board[index].team!=motion.piece.team):
                    k_attack=attack(damaged=index,dmg_points=k_dmg_2)
                    k_move=move(motion,k_attack)
                    total_moves.append(k_move)
    #Steady attack
    if pos_diff==0:
        k_attack=attack(damaged=None,dmg_points=k_dmg_3)
        k_move = move(motion,k_attack)
        for cell in neighbours(motion.final_position):
            for index in range(len(board)):
                if (board[index].position == cell)&(board[index].team!=motion.piece.team):
                    k_attack.damaged.append(index)
                    k_move = move(motion, k_attack)
        total_moves.append(k_move)
    return total_moves

def mage_attack(board,motion):
    total_moves=[]
    if motion.piece.position==motion.final_position:
        m_cure = attack(damaged=None, dmg_points=m_dmg_1)
        for cell in neighbours(motion.final_position):
            for index in range(len(board)):
                if (board[index].position == cell)&(board[index].team==motion.piece.team):
                    m_cure.damaged.append(index)
                    m_move = move(motion, m_cure)
                    total_moves.append(m_move)
    else:
        m_attack = attack(damaged=None,dmg_points=m_dmg_2)
        for index in range(len(board)):
            if board[index].team!=motion.piece.team:
                if manhattan_distance(board[index].position,motion.final_position)>m_dist_1:
                    m_attack = attack(damaged=index, dmg_points=m_dmg_2)
                    m_move = move(motion, m_attack)
                    total_moves.append(m_move)
    return total_moves

def archer_attack(board,motion):
    if motion.final_position==motion.piece.position:
        archer_damage = a_dmg_1
    else:
        archer_damage = a_dmg_2
    total_moves=[]
    for index in range(len(board)):
        token = board[index]
        ##Check orthogonal lines
        if (token.position[0]==motion.final_position[0])&(board[index].team!=motion.piece.team):
            if (not obstacle_in_the_way(board,token.position,motion.final_position,1))&(manhattan_distance(token.position,motion.final_position)>a_dist_1):
                a_attack = attack(damaged=index,dmg_points=archer_damage)
                a_move = move(motion,a_attack)
                total_moves.append(a_move)
        if (token.position[1]==motion.final_position[1])&(board[index].team!=motion.piece.team):
            if (not obstacle_in_the_way(board,token.position,motion.final_position,0))&(manhattan_distance(token.position,motion.final_position)>a_dist_1):
                a_attack = attack(damaged=index,dmg_points=archer_damage)
                a_move = move(motion,a_attack)
                total_moves.append(a_move)
        ## Check diagonal
        if (abs(token.position[0]-motion.final_position[0])==abs(token.position[1]-motion.final_position[1])):
            a_attack = attack(damaged=index, dmg_points=archer_damage)
            a_move = move(motion, a_attack)
            total_moves.append(a_move)
    return total_moves

def available_attacks(board,motion):
    if motion.piece.type == 1:
        return knight_attack(board,motion)
    if motion.piece.type == 2:
        return mage_attack(board,motion)
    if motion.piece.type == 3:
        return archer_attack(board,motion)

def main():
    k1=piece(1,1,30,(5,0))
    movimiento = motion(k1,(5,0))
    attack=archer_attack(initial_board,movimiento)
    duo = []
    #print(obstacle_in_the_way(initial_board,(2,3),(7,3),0))
    #print('Pieza atacable: ', initial_board[attack[0].attack.damaged[0]].type,'-',initial_board[attack[0].attack.damaged[0]].team,' Puntos de herida: ', attack[0].attack.dmg_points)
    #print('Pieza curable: ', initial_board[attack[1].attack.damaged[0]].type,'-',initial_board[attack[1].attack.damaged[0]].team, ' Puntos de herida: ',attack[0].attack.dmg_points)
    #print('Pieza curable: ', initial_board[attack[2].attack.damaged[0]].type, '-',initial_board[attack[1].attack.damaged[0]].team, ' Puntos de herida: ', attack[0].attack.dmg_points)

if  __name__ =='__main__':
    main()




