from copy import copy

prices = [17, 54.5, 198.99, 617, 1045, 754.04, 12, 5, 99.09, 70]
print_prices = []


for price in prices:
    roubles = round(price * 10 // 10)
    pennies = round((price - roubles) * 100)
    print_prices.append('{0} руб {1:02d} коп'.format(roubles, pennies))

print(', '.join(print_prices))

print(f'\nId of prices list before sort: {id(prices)}')

idx = 0
prices.sort()
while idx < len(prices):
    price = prices[idx]
    roubles = round(price * 10 // 10)
    pennies = round((price - roubles) * 100)
    prices[idx] = ('{0} руб {1:02d} коп'.format(roubles, pennies))
    idx += 1

print(', '.join(prices))
print(f'Id of prices list after sort: {id(prices)}\n')

print('Reversed prices')
prices_reverse = prices[::-1]
print(', '.join(prices_reverse))

print('\nTop-5')
print(', '.join(prices_reverse[:5][::-1]))
