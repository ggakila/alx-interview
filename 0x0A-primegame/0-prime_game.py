#!/usr/bin/python3
""" Module for solving prime game question """

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes to generate list of prime numbers."""
    primes = []
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, n+1, i))
    return primes

def isWinner(x, nums):
    """Check for the winner of the game."""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        if len(primes) % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

