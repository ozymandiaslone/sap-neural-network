from nnet import Nnet
import numpy as np
import random

class Players():
    def __init__(self, turn, board, nnet1=None, nnet2=None):
        self.fitness = 0
        self.turn = turn
        self.board = board
        if nnet1 is not None and nnet2 is not None:
            self.nnet = Nnet(12,50,36,nnet1, nnet2)
        else:
            self.nnet = Nnet(12, 50, 36)

    

    def reset(self):
        self.fitness = 0
    
    def query(self, board):
        self.board = board
        return self.nnet.get_outputs(board)
       
    def update_after_choice(self, spent, turn, lives_lost):
        if turn:
            self.turn += 1
        self.fitness += spent
        self.fitness -= lives_lost
              

    def create_offspring(p1,p2):
        new_player = Players(0, p1.board)
        new_player.nnet.create_mixed_weights(p1.nnet, p2.nnet)
        return new_player
    
    def create_new_generation(self):
        self.players = []
        for i in range(0, 10):
            self.players.append(Players(i, self.board))

    def evolve_population(self, gen):
        for b in gen:
            b.fitness += b.turn 

        gen.sort(key=lambda x: x.fitness, reverse=True)
        for g in gen:
            print("fitness: " + str(g.fitness))

        cut_off = int(len(gen) * 0.3)
        good_players = gen[:cut_off]
        bad_players = gen[cut_off:]
        num_bad_to_take = int(len(gen) * 0.1)
        
        for i in bad_players:
            i.nnet.modify_weights()
        
        new_players = []

        idx_bad_to_take = np.random.choice(np.arange(len(bad_players)), num_bad_to_take, replace=False)

        for i in idx_bad_to_take:
            new_players.append(bad_players[i])
        
        new_players.extend(good_players)
    
        #childredn_req = len(self.players) - len(new_players)

        while len(new_players) < len(gen):
            idx_to_breed = [[None],[None]]
            idx_to_breed[0] = random.randint(0, len(good_players)-1)
            idx_to_breed[1] = random.randint(0, len(good_players)-1)
            print("Idx_to_breed:")
            print(idx_to_breed)
            if idx_to_breed[0] != idx_to_breed[1]:
                print(len(good_players))
                print(good_players[idx_to_breed[0]])
                print(good_players[idx_to_breed[1]])
                new_player = Players.create_offspring(good_players[idx_to_breed[0]], good_players[idx_to_breed[1]])
                if random.random() < 0.4:
                   new_player.nnet.modify_weights() 
                new_players.append(new_player)

        for i in new_players:
            i.reset()
        
        gen = new_players
        return gen

        