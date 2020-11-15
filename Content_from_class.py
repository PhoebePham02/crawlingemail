import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import re
import requests
url='https://www.hisvietnam.com/about/our-faculty'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
div=soup.find_all('a',attrs={'class':'fsConstituentProfileLink'})
name=[]
for a in div:
    name.append(a.get_text())
name_list=pd.DataFrame(name)
name_list.to_csv('name_his.csv')
print(name_list)