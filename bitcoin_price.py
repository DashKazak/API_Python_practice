import requests
from pprint import pprint
coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(coindesk_url)
data = response.json()
print(data)

dollars_exchange = data['bpi']['USD']['rate_float']
print(dollars_exchange)

bitcoin = float(input('Your bitcoin amount: '))
bitcoin_value_dollars = bitcoin*dollars_exchange
print(f'{bitcoin} is equal to {bitcoin_value_dollars} for you')