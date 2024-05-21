import requests


def convert_gbp_to_usd(amount):
    response = requests.get('https://v6.exchangerate-api.com/v6/ed08d85b3bdeb9518f7a540b/latest/GBP')
    exchange_rates = response.json()['conversion_rates']
    # print(exchange_rates)
    usd_rate = exchange_rates['USD']
    usd_amount = amount * usd_rate
    return usd_amount


# usd_rate = 1.31

pounds = float(input())
dollars = convert_gbp_to_usd(pounds)
print(f'{dollars:.3f}')
