import requests
from pprint import pprint
from bs4 import BeautifulSoup

#BTC SCRAPPING

btc = requests.get("https://www.binance.com/en-IN/price/bitcoin")
soupbtc = BeautifulSoup(btc.content, "html.parser")

namebtc = soupbtc.find('div',class_="css-3wramu")
pricebtc = soupbtc.find('div',class_="css-12ujz79")

namebtc=namebtc.text
pricebtc=pricebtc.text

print(pprint(namebtc))
print(pprint(pricebtc))

#ETH SCRAPPING

eth = requests.get("https://www.binance.com/en-IN/price/ethereum")
soupeth = BeautifulSoup(eth.content, "html.parser")

nameeth = soupeth.find('div',class_="css-3wramu")
priceeth = soupeth.find('div',class_="css-12ujz79")

nameeth=nameeth.text
priceeth=priceeth.text


print(pprint(nameeth))
print(pprint(priceeth))

#LTC SCRAPPING

ltc = requests.get("https://www.binance.com/en-IN/price/litecoin")

soupltc = BeautifulSoup(ltc.content, "html.parser")

nameltc = soupltc.find('div',class_="css-3wramu")
priceltc = soupltc.find('div',class_="css-12ujz79")

nameltc=nameltc.text
priceltc=priceltc.text


print(pprint(nameltc))
print(pprint(priceltc))

