""" 
Calculate the probability of getting a specific sum throwing certain number of dices.
"""
import itertools
from collections import Counter
from fractions import Fraction

def throw_dices(*, num, sides ,throws=2, log_to_console=False):
    """
    ----------------------------------------------
    Parameters:

    'num' is the expected sum.
    'sides' is the number of sides of the dice. 
    'throws' is the amount of dices thrown.
    'log_to_console' gives you information about comb, Dsum, freq.
    ----------------------------------------------

    This func creates a list of lists that contain all the possible 
    combinations of dices taking into considerations the number of 
    sides and throws. Then, it gets the sum of each combination to 
    obtain its frequency and divide this number by the total number 
    of possibilities. 
    """

    # Create a dice of n sides
    dice = [i for i in range(1, sides+1)]

    # Create a list 'Dsum' that contains the sum of each possible combination of dices
    # Create a dictionary 'freq' which counts the frequency of each element on the list 'Dsum'
    comb = list(itertools.product(dice, repeat=throws))
    Dsum = list(map(sum, comb))
    freq = Counter(Dsum)
        
    
    if log_to_console:
        print("The possible combinations are:\n", comb, "\n", sep = "")
        print("The sum of each combination is:", Dsum, "\n", sep = "")
        print("The frequency of each sum is:\n", freq, "\n", sep = "")

    prob = round(freq[num] / len(comb) * 100, 2)
    frac = Fraction(freq[num], len(comb)).limit_denominator(10000)
    print(f'The probability of getting the sum of {num} with {throws} dices of {sides} sides is {prob}% or {frac}')

throw_dices(num=12, sides=6, throws=3)
