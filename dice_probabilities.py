from fractions import Fraction
from collections import Counter

def get_dice_comb_prob(num, sides, throws=2, log_to_console=False):
    """
    Prints the probability (in fractions and
    percentage) of getting a specific sum throwing 
    certain number of dices (of various sides).

    ----------------------------------------------

    Parameters:

    'num' is the expected sum.
    'sides' is the number of sides of the dice. 
    'throws' is the amount of dice thrown.
    'log_to_console' gives you information if True

    ----------------------------------------------

    This func creates a list of lists that contain 
    all the possible combinations of dices taking into 
    considerations the number of sides and throws. 
    Then, it gets the sum of each combination to 
    obtain its frequency and divide this number
    by the total number of possibilities. """

    a, b, c = 1, 1, 1
    comb = [[] for n in range(sides**throws)]

    for n in range(len(comb)):
        comb[n].append(a)
        comb[n].append(b)
        b += 1
        
        if (n+1) % sides == 0:
            a += 1
            b = 1
            if a > sides:
                a = 1

    for i in range(throws-2, 0, -1):
        for n in range(len(comb)):
            comb[n].append(c)
            if (n+1) % int(len(comb)/sides**(i)) == 0:
                c += 1
                if c > sides: 
                    c = 1

    # Create a list 'Dsum' that contains the sum of each possible combination of dices
    # Create a dictionary 'freq' which counts the frequency of each element on the list 'Dsum'
    Dsum = list(map(sum, comb))
    freq = Counter(Dsum)

    if log_to_console:
        print("The possible combinations are:\n", comb, "\n", sep = "")
        print("The sum of each combination is:", Dsum, "\n", sep = "")
        print("The frequency of each sum is:\n", freq, "\n", sep = "")
    
    prob =  round(freq[num]/sum(freq.values()) * 100, 2)
    fraction = Fraction(freq[num], sum(freq.values())).limit_denominator(10000)
    print(f'The probability of getting the sum of {num} with {throws} dices of {sides} sides is {prob}% or {fraction}')

get_dice_comb_prob(2, 2, 2)