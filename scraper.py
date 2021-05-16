#Reference: https://gist.github.com/suriyadeepan/b940caf6cba552527613c1f93e26cc80

import requests
from bs4 import BeautifulSoup

imgContent = requests.get(url='https://en.wikipedia.org/wiki/City').content

soup = BeautifulSoup(imgContent, 'html.parser')

imgs = soup.find_all('img')

for img in imgs:
	print(img.get('src'))

textContent = requests.get(url = 'https://en.wikipedia.org/wiki/City').content

soup = BeautifulSoup(textContent, 'html.parser')

texts = soup.find_all('a')
for text in texts:
	print(text.get('href'))
