import random

from graph import BuildScaleFree

# Implements a player using the WSLpS strategy
class Player:
    def __init__(self,choice,alpha):
        self.choice = choice
        self.alpha = alpha

    def Update(self,utility,best):
        if utility == 0 and random.random() < self.alpha:
            self.choice = best


def same_strategy(players):
    c = players[0].choice
    return [c for i in players] == [i.choice for i in players]

def Convention(graph,n,iters):
    j = 0
    players = [Player(random.randint(0,1),.5) for i in range(0,n)]
    while j < iters:

        if same_strategy(players):
            return j
        p_one = random.randint(0,n - 1)
        p_two = graph.GetRandomNeighbor(p_one)
        c_one = players[p_one].choice
        c_two = players[p_two].choice
        if c_one != c_two:
            players[p_one].Update(0,c_two)
            players[p_two].Update(0,c_one)

        j += 1
    return iters
