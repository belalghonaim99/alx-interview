#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Making changes needed
    Args: 
        coins: list of coins
        total: total amount
    
    """
    if total <= 0:
        return 0
    checking = 0
    start = 0
    coins.sort(reverse=True)
    for i in coins:
        while checking < total:
            checking += i
            start += 1
        if checking == total:
            return start
        checking -= i
        start -= 1
    return -1
