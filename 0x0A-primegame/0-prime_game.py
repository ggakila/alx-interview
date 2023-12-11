#!/usr/bin/python3
"""Module for solving the prime game question."""

def is_winner(x, nums):
    """Determine the winner of the prime game.

    Args:
        x (of type int): represents the number of rounds.
        nums (of type list): Numbers representing the game rounds.

    Returns:
        str: Returns Ben or Maria based on who won the most rounds or None if tied.
    """
    if not nums or x < 1:
        return None

    largest_number = max(nums)
    prime_filter = [True] * max(largest_number + 1, 2)
    for i in range(2, int(pow(largest_number, 0.5)) + 1):
        if not prime_filter[i]:
            continue
        for j in range(i * i, largest_number + 1, i):
            prime_filter[j] = False
    prime_filter[0] = prime_filter[1] = False

    prime_count = 0
    for i in range(len(prime_filter)):
        if prime_filter[i]:
            prime_count += 1
        prime_filter[i] = prime_count

    maria_wins = 0
    for number in nums:
        maria_wins += prime_filter[number] % 2 == 1

    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"


