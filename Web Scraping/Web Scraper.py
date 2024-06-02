from bs4 import BeautifulSoup
import requests
url = 'https://sites.google.com/view/technowizards/home'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
print(soup)
