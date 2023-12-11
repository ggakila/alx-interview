#!/usr/bin/python3


def is_prime(n):
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True

def isWinner(x, nums): 
    winner_counter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        round_winner = is_round_winner(nums[i], x)
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None


def is_round_winner(n, x):
    number_list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        selected_indices = []
        prime = -1

        for idx, num in enumerate(number_list):
            if prime != -1:
                if num % prime == 0:
                    selected_indices.append(idx)
            else:
                if is_prime(num):
                    selected_indices.append(idx)
                    prime = num

        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selected_indices):
                del number_list[val - idx]

    return None


