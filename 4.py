import sys

from utils import get_currency

currency, date = get_currency(sys.argv[1])
print(f'{currency}, {date}')