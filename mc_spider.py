from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.moneycontrol.com/").text
soup = BeautifulSoup(source,'lxml')

left_news_div = soup.find('div',class_='clearfix ltsnewsbx')
print('Headline::::',left_news_div.h1.a.text)
print('HREF::::',left_news_div.h1.a['href'])
print('Description::::',left_news_div.p.text)

ul_tag = soup.find('div',class_='clearfix ltsnewsbx').ul
li_list = ul_tag.find_all('li')
for li in li_list:
    print(li.text,li.a['href'])