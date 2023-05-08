import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div', attrs = {'class':'_2kHMtA'}):
    title = d.find('div',attrs = {'class':'_4rR01T'} )
    
    price = d.find('div',attrs = {'class':'_30jeq3 _1_WHN1'}) 
    
    image = d.find('img', attrs = {'class':'_396cs4'})
    
    #print(image.get('src'))
    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get( 'src' ))
    

data = {"TTILES":titles,
        "PRICES":prices,
        "IMAGES":images}

df = pd.DataFrame(data)

print(df)


df.to_excel('Camera.xlsx')