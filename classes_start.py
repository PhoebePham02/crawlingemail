import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import pandas as pd
link=[]
url ='https://www.nordangliaeducation.com/our-schools/vietnam/ho-chi-minh-city/bis/our-staff'
parts = urlsplit(url)
base_url = "{0.scheme}://{0.netloc}".format(parts)
response = requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
links = [a.attrs.get('href') for a in soup.select('a[href]') ]
new_link=list(filter(lambda x: ('staff' in x),links))
allLinks=list(map(lambda x: base_url+x, new_link))
emails=set()

for link in allLinks:
    r=requests.get(link)
    data=r.text
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", 
                  data, re.I)) # re.I: (ignore case)
    emails.update(new_emails)
a=pd.DataFrame(emails)
print(a)


