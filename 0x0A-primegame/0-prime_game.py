#!/usr/bin/python3

""" Prime Game """

def isWinner(x, nums):
<<<<<<< HEAD
=======
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the upper bounds for each round.

    Returns:
        str or None: The name of the player that won the most rounds. None if the winner cannot be determined.
    """

>>>>>>> a297e796e783342dd532f40b9d8f6717d7587e06
    def generate_primes(n):
        primes = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes[p]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = generate_primes(n)
        turn = 0
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            if not primes:
                if turn % 2 == 0:
                    maria_wins += 1
                else:
                    ben_wins += 1
            turn += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
