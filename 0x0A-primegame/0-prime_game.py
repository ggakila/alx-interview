#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def play_game(n):
    primes = [i for i in range(2, n+1) if is_prime(i)]
    turn = 0  
    while primes:
        chosen_prime = primes[0]
        primes = [p for p in primes if p % chosen_prime != 0]
        turn = 1 - turn  
    return turn  

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None