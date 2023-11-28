#!/usr/bin/python3
""" makechange challenge """


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1

    return coin_count if total == 0 else -1

