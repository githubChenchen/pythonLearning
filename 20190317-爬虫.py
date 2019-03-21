import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.d28k.com/cn/vl_genre.php?g=ne')
print(r.status_code)
r.encoding = 'utf-8'
soup=BeautifulSoup(r.text,"html.parser")
for list in soup.find_all('div',{'class':'id'}):
    if not list.string == None:
        print(list.string)
