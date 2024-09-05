def isWinner(x, nums):
    """
    Args:
        x (int): Number of rounds
        nums (array): Contains ranges on which the game is played on

    Return (str): The name of the player won the most
    """
    if x == 0 or not nums:
        return None

    def findPrimes(n):
        """Returns a list of primes up to n using the Sieve of Eratosthenes"""
        if n < 2:
            return []
        n += 1
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
        return [i for i in range(2, n) if is_prime[i]]

    def playGame(n):
        """Simulates the game and returns the winner"""
        if n < 2:
            return "Ben"

        primes = findPrimes(n)
        available = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        
        while primes:
            prime = primes[0]
            if prime > n:
                break

            if prime in available:
                # Remove prime and its multiples
                to_remove = set()
                for multiple in range(prime, n + 1, prime):
                    to_remove.add(multiple)
                available.difference_update(to_remove)
                
                # Remove used prime
                primes = [p for p in primes if p not in to_remove]
            else:
                primes.pop(0)  # Skip this prime

            # Check if anyone can make a move
            if not any(p in available for p in primes):
                if turn == 0:
                    return "Ben"
                else:
                    return "Maria"

            # Switch turn
            turn = 1 - turn
        
        # If no more moves
        return "Ben" if turn == 0 else "Maria"

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = playGame(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

