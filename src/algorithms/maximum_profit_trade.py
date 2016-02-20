## Objective
##   Write an function to find the maximum possible profit
## Input
##   A list of closing prices of a stock for the past few days
##   e.g. [10, 7, 5, 8, 11, 9]
## Constraints and clarifications
##   You can buy / sell at the closing price at close of market hours on that day
##   You will buy and sell only one unit of stock
##   You can sell only after you buy
##   You can not buy and sell on the same day
## Output
##   6
## Explanation
##   In the sample input, you would make maximum profit of 6 if you buy at 5 and sell at 11
## References

def max_profit(A):
  if len(A) < 2:
    raise Exception('Invalid input!')
  buy = A[0]
  profit = 0
  for i in range(1, len(A)):
    profit = max(profit, A[i] - buy)
    buy = min(buy, A[i])
  return profit

if __name__ == '__main__':
  A = [10, 7, 5, 8, 11, 9]
  print max_profit(A)
  assert 6 == max_profit(A)