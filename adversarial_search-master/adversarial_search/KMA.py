import adversarial_search
from adversarial_search.classes import *
from adversarial_search.mechanics import *
from adversarial_search.parameters import *
from adversarial_search.core import Game
from adversarial_search.core import match,run_match
from adversarial_search.utils import game_result



PLAYERS = ('Good','Bad')



class KMA (Game):
    knight_1 = piece(1, 1, PARAM.k_hp, (0, 3))
    mage_1 = piece(1, 1, PARAM.m_hp, (0, 2))
    archer_1 = piece(1, 1, PARAM.a_hp, (0, 1))
    knight_2 = piece(2, 1, PARAM.k_hp, (8, 3))
    mage_2 = piece(2, 1, PARAM.m_hp, (8, 2))
    archer_2 = piece(2, 1, PARAM.a_hp, (8, 1))

    initial_board = [knight_1, mage_1, archer_1, knight_2, mage_2, archer_2]



    def __init__(self,board=initial_board,enabled=0):
        Game.__init__(self,*PLAYERS)
        self.board = board
        self.enabled=enabled


    def active_player(self):
        return self.players[self.enabled]

    def moves(self):
        tot_moves = []
        av_motion = adversarial_search.mechanics.available_motion(self.board,self.enabled)
        for motion in av_motion:
            tot_attacks = adversarial_search.mechanics.available_attacks (self.board,motion)
            for one_attack in tot_attacks:
                tot_moves.append(one_attack)
        return tot_moves

    def next(self,move):
        aux_board = self.board
        ##Perform the motion of the token
        for token in aux_board:
            if token.position == move.motion.piece.position:
                token.position = move.motion.final_position
        ##Perform the action of attacking
        for damaged in move.attack.damaged:
            aux_board[damaged].health-=move.attack.dmg_points
        ##Undertaker
        for token in aux_board:
            if token.health<=0:
                del token
        return KMA(board=aux_board,enabled=(self.enabled + 1) % 2)

    def results(self):
        hp_1 = 0
        hp_2 = 0
        for token in self.board:
            if token.team == 1:
                hp_1+=token.health
            if token.team == 2:
                hp_2+=token.health
        if hp_1 <=0 or hp_2 <=0:
            return game_result('Good', self.players, (hp_1 - hp_2)/abs((hp_1 - hp_2)))
        else:
            return None

#########################################
# Test
#########################################

def test_game():
    from adversarial_search.agents.random import RandomAgent
    from adversarial_search.agents.mcts import MCTSAgent
    PARAM.set_parameters(30,12,10,5,30,20,4,5,30,2,1,2)
    game = KMA()
    agent0 = RandomAgent(name='Player 0')
    agent1 = RandomAgent(name='Player 1')
    agent2 = MCTSAgent (name = 'MonteCarlo',simulationCount=1000)
    for move_number, moves, game_state in match(game, agent2, agent1):
        if move_number is not None:
            None
        else:
            print(moves)
            

#def main():
#    test_game()

#if  __name__ =='__main__':
#    main()

