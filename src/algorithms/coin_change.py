## Objective
##   Write an function to find the minimum number of coins for giving change
## Input
##   A list of available coins & an amount
##   e.g. [1, 5, 10, 21, 25] & 63
## Constraints and clarifications
##   - There is infinite supply of coins of each type
## Output
##   3
## Explanation
##   In the sample input, you would make maximum profit of 6 if you buy at 5 and sell at 11
## References
##   [Coin change](http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html)

def coins(n, C, A):
  if n in C:
    A[n] = 1
  if not A[n]:
    A[n] = min([1 + coins(n-c, C, A) for c in C if c < n])
  return A[n]
C = [1, 5, 10, 21, 25]
n = 63
A = [0] * (n+1)
print coins(n, C, A)
assert 3 == coins(n, C, A)