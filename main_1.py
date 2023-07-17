from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
product_names = []
prices = []

for a in doc.find_all('a', href=True, attrs={'class': '_1fQZEK'}):
    name = a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    product_names.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({'Product Name': product_names, 'Price': prices})
df.to_csv('products.csv', index=False, encoding='utf-8')

