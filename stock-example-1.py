# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:17:49 2020

@author: JP
"""

import requests
from bs4 import BeautifulSoup

class bond(object):
    def __init__(self): 
         self.__name=[]
         self.__value=[]
        
    def search(self, object1):
        if object1 == 'EXAMPLE1':  # EXAMPLE1 is a placeholder for the name of the bond, you want to search, for example the ETF 'A1JX52'
            r=requests.get('EXAMPLE2') # EXAMPLE2 is a placeholder for the website, on which the value of the bond is available..e.g. 'https://EXAMPLE.com'
            soup=BeautifulSoup(r.text, 'html.parser')
            #print(soup)
            self.__value=soup.find(id="EXAMPLE3") # EXAMPLE3 is a placeholder for the id which refer to the value of the bond, e.g. 'u_385016294', you can find it in the source code of the website
            self.__name=object1
            print(self.__value.text)

    def get_value(self):
        return self.__value.text
    
    def get_name(self):
        return self.__name
    