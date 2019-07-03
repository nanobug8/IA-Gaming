import random
import copy
import available_moves


class Game(object):  ################################################################################
    """ Base class for all game components. The instance represents a game state, including
        information about the board, the pieces, the players and any other data required to continue
	   the game.
    """

    def __init__(self, *players):
        """ The constructor initializes the object to represent the game's initial state. Players
            list indicates the players that will participate in the game. These are not the actual
            agents in charge of moving, but only their role. Examples are 'Xs' and 'Os' or 'Whites'
            and 'Blacks'. Subclasses must support an empty or None players parameter, indicating a
            default option. A player may be any hashable type, but str is recommended.
        """

        self.players = players

    def active_player(self):
        """ Returns the player enabled to make moves in the current game state.
        """
        raise NotImplementedError('Class %s has not implemented method active_player.' % self.__class__.__name__)

    def moves(self):
        """ Returns all valid moves in the game state for the active player. If the game has
            finished, it should be an empty sequence.
        """

        raise NotImplementedError('Class %s has not implemented method moves.' % self.__class__.__name__)

    def results(self):
        """ Returns the results of a finished game for every player. This will be a dict of the form
            `{player:float}`. Draws are always 0, with victory results being always positive and
		  defeat always negative. Must return an empty dict if the game is not finished.
        """
        raise NotImplementedError('Class %s has not implemented method results.' % self.__class__.__name__)

    def next(self, move):
        """ Calculates and returns the next game state applying the given move. The moves parameter
            is one of the values returned by the moves method. Result should be None if any move is
            invalid or game has ended.
        """
        raise NotImplementedError('Class %s has not implemented method next.' % self.__class__.__name__)

    def __hash__(self):
        return hash(repr(self))


class Agent(object):  ###############################################################################
    """ Base class for agents participating in games.
    """

    def __init__(self, name):
        self.name = name
        self.player = None

    def decision(self, game, *moves):
        """ Agents move choice. If no moves are provided, choices are retrieved from the game.
        """
        if not moves:
            moves = game.moves()
            if not moves:
                return None
        return self._decision(moves)

    def _decision(self, moves):
        """ Method called by Agent.decision() to actually make the choice of move. This should be
            overriden by subclasses.
        """
        return moves[0]  # Please do not use this default implementation.

    def match_begins(self, player, game):
        """ Tells the agent that a match he is participating in is starting. This should not be
            called again until the match ends.
        """
        self.player = player

    def match_moves(self, before, move, after):
        """ Tells the agent the active player have moved in the match he is participating in.
        """
        pass

    def match_ends(self, game):
        """ Tells the agent the match he was participating in has finished. The game parameter holds
            the final game state.
        """
        pass

    def __str__(self):
        return '%s(%s)' % (self.name, self.player)

    def __hash__(self):
        return self.name.__hash__()

    def randgen(self, x):
        """ If x is `None` or `int` or `long`, returns random.Random(x), else returns x.
        """
        return random.Random(x) if x is None or type(x) == int else x

    # Match ############################################################################################


def match(game, *agents_list, **agents):
    """ A match controller in the form of a generator. Participating agents can be specified either
        as a list (agents_list) or pairs player=agent. If the list is used, agents are assigned in
        the same order as the game players.

        The generator returns tuples. First `(0, agents, initial game state)`. After that
	   `(move_number, move, game state)` for each move. Finally `(None, results,
	   final game state)`. The generator handles the match, asking the enabled agents to move,
        keeping track of game states and notifying all agents as needed.
    """
    for player, agent in zip(game.players, agents_list):
        agents[player] = agent
    for player, agent in agents.items():  # Tells all agents the match begins.
        agent.match_begins(player, game)
    move_num = 0
    yield (move_num, agents, game)
    results = game.results()
    while not results:  # Game is not over.
        chosen_move = agents[game.active_player()].decision(game)
        next_game = game.next(chosen_move)
        for player, agent in agents.items():  # Tells all agents about the moves.
            agent.match_moves(game, chosen_move, next_game)
        game = next_game
        move_num += 1
        yield (move_num, chosen_move, game)
        results = game.results()
    for player, agent in agents.items():  # Tells all agentes the match ends.
        agent.match_ends(game)
    yield (None, results, game)


def run_match(game, *agents_list, **agents):
    """ Runs a full match returning the results and final game state.
    """
    for m, d, g in match(game, *agents_list, **agents):
        if m is None:  # Game over.
            return (d, g)
    return (None, game)  # Should not happen.


class RandomAgent(Agent):
    """ An agent that moves randomly.
    """

    def __init__(self, random=None, name='RandomAgent'):
        Agent.__init__(self, name)
        # An instance of random.Random or equivalent is expected, else an
        # integer seed or None to create a random.Random.
        self.random = self.randgen(random)

    def _decision(self, moves):
        return self.random.choice(moves)



class KMA (Game):
    initial_board = [[1,1,[0,1],30],[1,1,[0,2],30],[1,1,[0,3],30],[2,1,[1,1],30],[2,1,[8,2],30],[2,1,[8,3],30]]
    initial_dict = {1: {"k_dmg_1": 1, "k_dmg_2": 2, "k_dmg_3": 8}, 2: {"m_dmg_1": 1, "m_dmg_2": 2, "m_dist_1": 8},
            3: {"a_dmg_1": 1, "a_dmg_2": 2, "a_dist_2": 8}}

    PLAYERS = ('Good','Bad')

    def init(self, board=initial_board, enabled=0, dict=initial_dict):
        Game.init(self, *KMA.PLAYERS)
        self.board = board
        self.dict = dict
        self.enabled = enabled

    def active_player(self):
        return self.players[self.enabled]

    def moves(self):
        if self.active_player() == 'Good':
            team_nmbr = 1
        else:
            if self.active_player() == 'Bad':
                team_nmbr = 2
        total_moves = available_moves.tucutucutucu(self.board, team_nmbr)
        print(total_moves)
        return total_moves


    def results(self):
        hp1 = self.board[0][1] + self.board[1][1] + self.board[2][1]
        hp2 = self.board[3][1] + self.board[4][1] + self.board[5][1]

        if hp1 == 0:
            result = -1
            return result
        if hp2 == 0:
            result = 1
            return result
        else:
            return None



    def next(self, move):
        #keep a copy of board. Aply magin on it, and return a new board for the game
        movio = o
        aux_board = copy.deepcopy(self.board)
        available_moves.move(move[0],move[1])
        if self.active_player() == 'Good':
            team_nmbr = 1
            if self.board[1] != aux_board[1]:
                movio = 1
        else:
            if self.active_player() == 'Bad':
                team_nmbr = 2
                if self.board[1] != aux_board[1]:
                    movio = 1

        if move[0] ==  available_moves.MAGUE:
            if movio:
                available_moves.heal(team_nmbr, self.board, self.dict[available_moves.MAGUE]['m_dmg_1'])
            else:
                if move[2] == 1:
                    #atack
                    available_moves.attack(move[3],self.dict[move[0]]['m_dmg_2'], self.board)

        if move[0] == available_moves.KNIGHT:
            if movio:
                piece = 0
                if team_nmbr == 2:
                    piece = 3
                if available_moves.manhattan_distance(self.board[piece], aux_board[piece]) < 2:
                    available_moves.attack(move[3],self.dict[move[0]]['k_dmg_1'], self.board)
                else:
                    available_moves.attack(move[3], self.dict[move[0]]['k_dmg_2'], self.board)
            else:
                available_moves.attack(move[3],self.dict[move[0]]['k_dmg_3'], self.board)

        if move[0] == available_moves.ARCHER:
            if movio:
                available_moves.attack(move[3], self.dict[move[0]]['a_dmg_2'], self.board)
            else:
                available_moves.attack(move[3],self.dict[move[0]]['a_dmg_1'], self.board)


        return KMA(aux_board, (self.enabled + 1) % 2)



def run_test_game(agent1=None, agent2=None):
    if not agent1:
        agent1 = RandomAgent(name='Bueno')
    if not agent2:
        agent2 = RandomAgent(name='Malo')
    run_match(KMA(), agent1, agent2)


def main():
    run_test_game()

if __name__ == 'main':
    main()