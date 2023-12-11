#!/usr/bin/python3

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    largest = max(nums)

    filtered_nums = [True for _ in range(max(largest + 1, 2))]
    for i in range(2, int(pow(largest, 0.5)) + 1):
        if not filtered_nums[i]:
            continue
        for j in range(i * i, largest + 1, i):
            filtered_nums[j] = False
    filtered_nums[0] = filtered_nums[1] = False
    y = 0
    for i in range(len(filtered_nums)):
        if filtered_nums[i]:
            y += 1
        filtered_nums[i] = y
    player1 = 0
    for x in nums:
        player1 += filtered_nums[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"