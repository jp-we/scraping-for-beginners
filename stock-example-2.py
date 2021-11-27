
import requests
from bs4 import BeautifulSoup
import locale

# Stock - Share Value
r=requests.get('XXX') # instead of XXX you have to fill in the website adress between the ''
soup = BeautifulSoup(r.text, 'html.parser')
value=soup.find_all(itemprop='price')[0] # this line is important: in the html code, you have to identify the position of the value you want to read out. In this case, the value has the itemprp "price". 
value=value.text.strip()
locale.setlocale(locale.LC_ALL, 'de_DE') # this line is optional but could be necessary..in my case the stock value has the format x,x and not x.x ... so we need to change this 
value= locale.atof(value) # also this line is optional but could be necessary
print('XXX: %(value1).2f' % {'value1':value}) # you can replace XXX with the name of the stock value, you want to display
