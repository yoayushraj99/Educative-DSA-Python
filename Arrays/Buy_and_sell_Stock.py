A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Time Complexity: O(n)
# Space Complexity: O(1)


def buy_and_sell_stock_once(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price)
    profit = price - min_price
    max_profit = max(profit, max_profit)
  return max_profit


print(buy_and_sell_stock_once(A))
