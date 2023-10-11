"""
Exercise 22 : Rock Paper Scissor
"""


def rps_check(p1, p2):
    """
    Check the result of a rock-paper-scissors game between two players.

    Parameters:
        p1 (str): The choice of player one. It can be 'rock', 'paper', or 'scissor'.
        p2 (str): The choice of player two. It can be 'rock', 'paper', or 'scissor'.

    Returns:
        str: The result of the game. It can be 'player one', 'player two', or 'tie'.
    """
    pl1 = 'player one'
    pl2 = 'player two'
    if (p1 == 'rock' and p2 == 'paper'):
        return pl2
    elif (p1 == 'rock' and p2 == 'scissors'):
       return  pl1
    elif (p1 == 'rock' and p2 == 'rock'):
        return 'tie'
    elif (p1 == 'paper' and p2 == 'rock'):
        return pl1
    elif (p1 == 'paper' and p2 == 'scissors'):
        return pl2
    elif (p1 == 'paper' and p2 == 'paper'):
        return 'tie'
    elif (p1 == 'scissors' and p2 == 'paper'):
        return pl1
    elif (p1 == 'scissors' and p2 == 'rock'):
        return pl2
    elif (p1 == 'scissors' and p2 == 'scissors'):
        return 'tie'
