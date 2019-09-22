from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # our base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # memoization
    return memo[n]



if __name__ == "__main__":
    print(fib3(5))
    print(fib3(50))
