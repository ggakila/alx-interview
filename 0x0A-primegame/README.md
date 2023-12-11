# Prime Game

## Overview

This Python script implements a two-player game where Maria and Ben take turns choosing prime numbers from a set of consecutive integers. The game is played in multiple rounds, with each round having a different range of integers. The winner of each round is determined based on the ability to make optimal moves and remove prime numbers and their multiples from the set.

## Function Signature

```python
def isWinner(x, nums):
    """
    Determine the winner of the prime game for each round.

    Args:
    - x (int): The number of rounds.
    - nums (list): An array of n for each round.

    Returns:
    - str or None: The name of the player that won the most rounds. If the winner cannot be determined, return None.
    """
    

