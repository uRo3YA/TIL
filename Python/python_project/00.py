import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers).json()
closing_price=response.get("data").get("closing_price")
print(closing_price)