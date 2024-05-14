#!/usr/bin/python3

""" Prime Game """


def isWinner(x, nums):
    def generate_primes(n):
        primes = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if primes[p] == True:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes[p]]
    # print(nums)
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
    # print(maria_wins, ben_wins)
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
