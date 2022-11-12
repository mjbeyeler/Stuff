# OLD
# Author: Michael J. Beyeler
# Takes any array (most often phenotypes in our case), and returns it as normally distributed based on the rank.
# Definition of rank: The lowest original value results in the lowest rank, etc
# 


import scipy.stats as ss

def rank_based_INT(a, stochastic = True):
    # GET RANK
    # method='average' is the default of ss.rankdata
    # The average rank of all the ranks assigned to the tied values is given to all of them.
    ranks = ss.rankdata(a, method='average')
    
    # RANK TO NORMAL
    # probit function on ranks, using c=3/8, which is what most people use
    c = 3/8
    x = (ranks - c) / (len(ranks) - 2*c + 1)
    return ss.norm.ppf(x)


