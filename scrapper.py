import requests
from pprint import pprint
from bs4 import BeautifulSoup

req = requests.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

soup = BeautifulSoup(req.content, "html.parser")

name = soup.find('div',class_="_4rR01T")
name=name.text
price = soup.find('div',class_="_30jeq3 _1_WHN1")
price=price.text

print(pprint(name))
print(pprint(price))