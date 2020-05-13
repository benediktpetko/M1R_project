# main.py
#%%
import numpy as np
from numpy.random import binomial
import matplotlib.pyplot as plt
import seaborn as sns


#%%
class gambler(object):

    def __init__(self, funds):
        self.history = np.array([funds])

    def play(self, g, rounds = 1):
        # generate Bernoulli outcomes
        b = binomial(1, 0.5 + g.edge , rounds)

        # generate random walk with step size being the bet of the game
        outcomes = self.history[-1] + np.cumsum(g.bet * ( (-1) ** (1+b) ) )

        # add the outcomes to gambler's history
        self.history = np.append(self.history, outcomes) 
    def plot_history(self):
        sns.lineplot(self.history)
        plt.show()

class game(object):
    def __init__(self, edge = -0.05, bet = 1):
        self.edge = edge
        self.bet = bet

#%%
if __name__=="__main__":
    np.random.seed(0)
    benedikt = gambler(100)
    g = game(edge=-0.05, bet =1)
    benedikt.play(10, g)
    benedikt.plot_history()