#!/usr/bin/python3
"""Module for solving the prime game question."""

def is_winner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None
    largets_num = max(nums)

    filtered_nums = [True for _ in range(max(largets_num + 1, 2))]
    for i in range(2, int(pow(largets_num, 0.5)) + 1):
        if not filtered_nums[i]:
            continue
        for j in range(i * i, largets_num + 1, i):
            filtered_nums[j] = False
    filtered_nums[0] = filtered_nums[1] = False
    y = 0
    for i in range(len(filtered_nums)):
        if filtered_nums[i]:
            y += 1
        filtered_nums[i] = y
    player_1 = 0
    for x in nums:
        player_1 += filtered_nums[x] % 2 == 1
    if player_1 * 2 == len(nums):
        return None
    if player_1 * 2 > len(nums):
        return "Maria"
    return "Ben"


